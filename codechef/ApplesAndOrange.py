#problemcode APPLORG
def ApporOrg(total, apple, orange):
    if apple+orange <= total:
        return "Yes"
    else:
        return "No"
        
if __name__ == "__main__":
    total = int(input())
    app, org = tuple(map(int, input().split()))
    print(ApporOrg(total, app, org))





