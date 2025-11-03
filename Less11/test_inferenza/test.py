import gradio as gr
import joblib
loaded_model = joblib.load('model_tips_stand.pkl')


def model_inferce(Total_Bill,Size):
    bill_st = (Total_Bill -19.78)/8.90
    size_st = (Size -2.56)/0.95
    y_pred = loaded_model.predict([[bill_st,size_st]])[0]
    return y_pred.round(2)


title = "Calcola la TIP yo! "
description = "This application calcolate the tip"

demo = gr.Interface(
                    fn=model_inferce,
                    inputs=["number", "number"],
                    outputs="number",
                    title=title,
                    description=description,
                    flagging_mode= "never",
                    )

demo.launch(share=True,debug=True)