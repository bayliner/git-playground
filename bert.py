from fastapi import FastAPI, APIRouter, HTTPException, status
from pydantic import BaseSettings
from sentence_transformers import SentenceTransformer, util

bert_router = APIRouter()

bertModel = SentenceTransformer('all-mpnet-base-v2')

#class BertClass:
    #def __init__(self,something):
        #self.something = something

    # def some_function(self):
    #     print(self.something)
        
#bertClass = BertClass("some_value")
#bertClass.some_function()


class BertInput(BaseSettings):
    compareA: str
    compareB: str

    class Config:
        schema_extra = {
            "example": {
                "compareA": "My name is jamie",
                "compareB": "CAll me jamie",
            }
        }


@bert_router.get("/sts")
#async def sts(bertInput: BertInput) -> dict:
async def sts() -> dict:
    # Two lists of sentences
    sentences1 = ['The cat sits outside',
                'A man is playing guitar',
                'The new movie is awesome',
                'My name is Jamie']

    sentences2 = ['The dog plays in the garden',
                'A woman watches TV',
                'The new movie is so great',
                "Call me Jamie"]

    #Compute embedding for both lists
    embeddings1 = bertModel.encode(sentences1, convert_to_tensor=True)
    embeddings2 = bertModel.encode(sentences2, convert_to_tensor=True)

    #Compute cosine-similarities
    cosine_scores = util.cos_sim(embeddings1, embeddings2)

    #Output the pairs with their score
    for i in range(len(sentences1)):
        print("{} \t\t {} \t\t Score: {:.4f}".format(sentences1[i], sentences2[i], cosine_scores[i][i])) 

    return {
        "message": "bertInput.compareA"
    }



@bert_router.get("/sts2")
async def sts(a: str, b: str) -> dict:
    bertInput = BertInput
    bertInput.compareA = a
    bertInput.compareB = b
    # Two lists of sentences
    sentences1 = [bertInput.compareA]

    sentences2 = [bertInput.compareB]

    #Compute embedding for both lists
    embeddings1 = bertModel.encode(sentences1, convert_to_tensor=True)
    embeddings2 = bertModel.encode(sentences2, convert_to_tensor=True)

    #Compute cosine-similarities
    cosine_scores = util.cos_sim(embeddings1, embeddings2)

    #Output the pairs with their score
    for i in range(len(sentences1)):
        print("{} \t\t {} \t\t Score: {:.4f}".format(sentences1[i], sentences2[i], cosine_scores[i][i])) 

    return {
        "Semantic Textual Similarity result": str.format("{:.4f}", cosine_scores[0][0])
    }
