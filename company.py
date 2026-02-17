from fastapi import FastAPI , Body

app = FastAPI()

companies = [
    {"name" : "Microsoft", "founder" : "Bill Gates", "category" : "Technology"},
    {"name" : "Amazon", "founder" : "Jeff Bezos", "category" : "Big tech"},
    {"name" : "Google", "founder" : "Larry Page", "category": "Multinational big tech"},
    {"name" : "Palantir", "founder" : "Peter theil", "category" : "Tech and Data analytics"}
]

@app.get("/companies")
async def get_company():
    return companies

# @app.get("/companies/{name_type}/")
# async def get_company(name_type: str):
#     for i in companies:
#         if i.get("name").casefold() == name_type.casefold():
#             return i


# @app.post("/create_company")
# async def get_company(new_company = Body()):
#     companies.append(new_company)
    
@app.put("/companies")
async def get_company(edit_company =  Body()):
    for i in range(len(companies)):
        if companies[i].get("name").casefold() == edit_company.get("name").casefold():
           companies[i] = edit_company
           return companies[i]
            
@app.delete("/companies/delete_company/{company_name}")
async def delete_company(company_name: str):
    for i in range(len(companies)):
        if companies[i].get("name").casefold() == company_name.casefold():
            companies.pop(i)
            break