raw_logs = []
processed_logs = []

def handle_input_value(records):
    table = str.maketrans("", "", "@!#$")
    print("--- NẠP DỮ LIỆU LOG ---")
    data = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ").strip().translate(table)
    list_data = data.split(";")
    for index, value in enumerate(list_data):
        list_data[index] = value.strip()
        if list_data[index] == '':
            list_data.pop(index)
    if list_data[-1] == '':
        list_data.remove('')
    records.extend(list_data)
    print(f"Đã làm sạch và lưu {len(list_data)} dòng log vào hệ thống.")
    print(records)

def find_error(log_list, records):
    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return
    search_list = [error for error in records if "ERROR" in error.upper() or "CRITICAL" in error.upper()]
    log_list.extend(search_list)
    if not log_list:
        print("Không có cảnh báo nguy hiểm nào")
        return
    print("--- LỌC CẢNH BÁO ---")
    print(f"Tìm thấy {len(log_list)} cảnh báo nguy hiểm:")
    print(log_list)


def processed_logs(records):
    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return
    for index, error in enumerate(records):
        records[index] = records[index].split(" ")
        for i,value in enumerate(records[index]):
            if value.count(".") == 3:
                records[index][i] = records[index][i].split(".")
                records[index][i][2] = "*"
                records[index][i][3] = "*"
                records[index][i] = ".".join(records[index][i])
        records[index] = " ".join(records[index])

    print(records)

def main():
    while True:
        choice = input("""
============= SECURITY LOG ANALYZER =============
1. Nhập và làm sạch dữ liệu Log thô
2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)
3. Mã hóa địa chỉ IP (Masking)
4. Đóng hệ thống
=================================================
Chọn chức năng (1-4): """) 
        
        if choice.isdigit():
            choice = int(choice)
        else:
            print("Vui lòng nhập số nguyên từ 1-4")
            continue
        
        match choice:
            case 1:
                handle_input_value(raw_logs)
                
            case 2:
                find_error(processed_logs, raw_logs)
                
            case 3:
                processed_logs(raw_logs)
            case 4:
                print("Thoát chương trình.")
                break
        
            case _:
                print("Lỗi cú pháp")
main()            
