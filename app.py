# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, make_response
from main_api import mint_to_user

# creating a Flask app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/

@app.route("/mint_nft", methods=["POST"])
def home():

    image_bin = request.form['img_bin']
    user_pub_key= request.form['user_pub_key']
    eye_form = request.form['get_eye']
    nose_form=request.form['get_nose']
    mouth_form=request.form['get_mouth']
    outfit_form=request.form['get_outfit']
    nft_num=request.form['nft_number']
    phone=request.form['phone_number']
    
    Nft_name,Tx_id = mint_to_user(image_bin,user_pub_key,eye_form,nose_form,mouth_form,outfit_form,nft_num,phone)

    tx= "https://explorer.solana.com/tx/"+ str(Tx_id)

    print(tx)

    final={
        "name": Nft_name,
        "transaction": tx
    }

    return jsonify(final)

# driver function
if __name__ == "__main__":

    app.run(debug=True)