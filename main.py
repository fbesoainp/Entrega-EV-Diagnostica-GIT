import json
import functions

data = [json.loads(line) for line in open('data/farmers-protest-tweets-2021-03-5.json', 'r')]

if __name__ == "__main__":
    while True:
        msg = """Seleccione funcion a ejecutar:\n
        1. Los top 10 tweets más retweeted\n
        2. Los top 10 usuarios en función a la cantidad de tweets que emitieron\n
        3. Los top 10 días donde hay más tweets\n
        4. Top 10 hashtags más usados\n
        5. Cerrar\n"""
        usr = input(msg)

        if usr != "5":
            if usr == "1":
                print(functions.topTweets(data))
            elif usr == "2":
                print(functions.topUsers(data))
            elif usr == "3":
                print(functions.topDays(data))
            elif usr == "4":
                print(functions.topHashtags(data))
            else:
                print("Input invalido\n")
        else:
            break
