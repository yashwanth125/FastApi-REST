from fastapi import FastAPI
app = FastAPI()
from databaseConnection import DatabaseConnection
dbConnection = DatabaseConnection()

#Get, Update, Delete, post

@app.get("/")
def result():
    return("FASTApi Server Running")


@app.get("/all_articles")
def get_all_articles():
    return dbConnection.get_all_articles()

@app.get("/article")
@app.get("/article/{articleId}")
def get_one_article(articleId:int):
    return dbConnection.get_one_article(articleId=articleId)

@app.delete("/article")
def delete_one_article(articleId:int):
    return dbConnection.delete_one_article(articleId=articleId)

@app.post("/article")
def post_article(body:dict):
    return dbConnection.post_article(articleJson=body)

@app.put("/article")
@app.put("/article/{articleId}")
def update_article(articleId:int, body:dict):
    return dbConnection.update_article(articleId=articleId, articleJson=body)


