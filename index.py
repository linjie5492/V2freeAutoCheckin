import main

def main_handler(event: dict, context: dict):
    msg = main.main()
    main.ftqq(msg)
    print("v2free自动签到！")
    return 0