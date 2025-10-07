
from flask import Flask, render_template, request, redirect, url_for,flash
import pyodbc

app = Flask(__name__)
app.secret_key = "cubetechworld_secret"
# SQL Server connection
#conn_str = (
 #  "DRIVER={ODBC Driver 17 for SQL Server};"
  # "Server=LAPTOP-R67CENEO\\MSSQLSERVER01;"  # replace with your server name
 #  "Database=CubeTechWorld;"        # replace with your DB name
 #  "Trusted_Connection=yes;"
#)
#conn = pyodbc.connect(conn_str)
def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOP-R67CENEO\\MSSQLSERVER01;"   # change this
        "DATABASE=CubeTechWorld;"                  # your DB name
        "Trusted_Connection=yes;"
    )



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/services')
def services():
    return render_template("services.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        message = request.form["message"]

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(

                "INSERT INTO ContactMessages (Name, Phone, Email, Message) VALUES (?, ?, ?, ?)",
                (name,phone,email, message)
                  
            )

            #print("Form Data:", name, phone, email, message)
            conn.commit()
            cursor.close()
            conn.close()
            flash("✅ Your message has been sent successfully!", "success")
        except Exception as e:
            flash(f"❌ Error: {str(e)}", "danger")
            print("❌ DB Error:", e)   # log in console

        return redirect(url_for("contact"))

    return render_template("contact.html")


    
if __name__ == "__main__":
    app.run(debug=True)
                        




            
            

            

        #cursor = conn.cursor()
        #cursor.execute("INSERT INTO ContactMessages (name,phone,email,message) VALUES (?, ?, ?, ?)", (name,phone,email,message))
        #conn.commit()
        #return redirect(url_for("contact"))
    #return render_template("contact.html")

#if __name__ == "__main__":
   # app.run(debug=True)
