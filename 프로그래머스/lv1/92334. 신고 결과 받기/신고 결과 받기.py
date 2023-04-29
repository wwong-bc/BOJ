def solution(id_list, report_list, k):
    answer = []
    # user dict : {user : {"report_user" : [], "reported_number" : reported_number}}
    user_dict = {user:{"report_user": [], "reported_number":0} for user in id_list}
    for report in report_list:
        user, reported = report.split()
        if reported not in user_dict[user]["report_user"]:
            user_dict[user]["report_user"].append(reported)
            user_dict[reported]["reported_number"] += 1
    for user in id_list:
        report_user = user_dict[user]["report_user"]
        mail_num = 0
        for rep_user in report_user:
            if user_dict[rep_user]["reported_number"] >= k:
                mail_num +=1
        answer.append(mail_num)
    return answer