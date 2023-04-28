import psycopg2
import json
import os


def GetQuestions():
    con = psycopg2.connect("dbname=tests user=api_robot password=1488")
    cur = con.cursor() 
    cur.execute("select to_json(data) from(select id, topic, ques from quest_raw)as data")
    question_data = cur.fetchall()
    cur.execute("select to_json(data) from(select ques_id, ans, is_correct from answ_raw )as data")
    answer_data = cur.fetchall()
    print()
    cur.close()
    con.close()
    to_json = {'Questions': question_data, 'Answers':answer_data}
    with open("payload.json", "w", encoding="utf-8") as file:
        json.dump(to_json, file, separators=(",", ":"),ensure_ascii=False, indent=4)
    file.close()
    return question_data, answer_data

    
GetQuestions()
