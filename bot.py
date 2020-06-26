from selenium import webdriver
from increase import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import login
import time

browser=webdriver.Chrome('.\\chromedriver.exe')

browser.get("https://www.instagram.com/")

time.sleep(2)


def follow(d):
    name="https://www.instagram.com/"+d
    browser.get(name)
    browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
    time.sleep(2)
    jscommand = """
    followers = document.querySelector(".isgrP");
    followers.scrollTo(0,followers.scrollHeight);
    var lenOfPage = followers.scrollHeight;
    return lenOfPage;
    console.log(lenofpage);
    """
    lenOfPage = browser.execute_script(jscommand)
    match=False
    while(match==False):
            lastCount = lenOfPage
            time.sleep(1)
            lenOfPage = browser.execute_script(jscommand)
            if lastCount==lenOfPage:
                match=True

    time.sleep(5)
    followersList = []
    followers = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

    for follower in followers:
        followersList.append(follower.text)
    return followersList







def following(d):
    name="https://www.instagram.com/"+d
    browser.get(name)
    browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
    time.sleep(2)
    jscommand = """
            followers = document.querySelector(".isgrP");
            followers.scrollTo(0,followers.scrollHeight);
            var lenOfPage = followers.scrollHeight;
            return lenOfPage;
            console.log(lenofpage);
            """
    lenOfPage = browser.execute_script(jscommand)
    match=False
    while(match==False):
            lastCount = lenOfPage
            time.sleep(1)
            lenOfPage = browser.execute_script(jscommand)
            if lastCount==lenOfPage:
                match=True

    time.sleep(5)
    followersList = []
    followers = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

    for follower in followers:
        followersList.append(follower.text)
    return followersList 
          


def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3



username = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
password = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")

username.send_keys(login.user)
password.send_keys(login.password)
time.sleep(2)
password.send_keys(Keys.ENTER)
time.sleep(6)
alert=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
alert.click()
time.sleep(4)
alert2=browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
alert2.click()  
time.sleep(2)

print("press 1 :- Your profile details")
print("press 2 :- another profile details")
print("press 3 :- comparison")
print("press 4 :- like some hastag")
print("press 5 :- comment hastag")










y=int(input())
if y==1 :
    name=login.user
    fer=[]
    fell=[]
    er=follow(name)
    fell=following(name)
    mutual=[]
    mutual=intersection(er,fell)
    print("you have" + str(len(er))+ "followers")
    print("you have" + str(len(fell))+ "followings")
    print("you have" + str(len(mutual))+ "mutuals")
if y==2:
    print("Enter the username")
    name=input()
    fer=[]
    fell=[]
    er=follow(name)
    fell=following(name)
    mutual=[]
    mutual=intersection(er,fell)
    print("you have" + str(len(er))+ "followers")
    print("you have" + str(len(fell))+ "followings")
    print("you have" + str(len(mutual))+ "mutuals")
if y==3:
    print("Enter the username1")
    name1=input()
    print("Enter the username2")
    name2=input()
    name1follow=[]
    name2follow=[]
    name1follow=follow(name1)
    name2follow=follow(name2)
    name1follow=name2follow.sort()
    name1follow=name2follow.sort()
    ans1=[]
    ans1=intersection(name1follow,name2follow)
    name1following=[]
    name2following=[]
    name1following=following(name1)
    name2following=following(name2)
    name1following=name2following.sort()
    name1following=name2following.sort()
    ans2=[]
    ans2=intersection(name1follow,name2follow)
    print(name1,end=" ")
    print(" have"+str(len(name1follow))+ "followers")
    print(name1,end=" ")
    print(" have"+str(len(name1following))+ "followings")
    print(name2,end=" ")
    print(" have"+str(len(name2follow))+ "followers")
    print(name2,end=" ")
    print(" have"+str(len(name2following))+ "followings")
    print("You both have "+ str(len(ans1))+ "followers and "+ str(len(ans2))+"followings" )
if y==4:
    print("enter the Hashtag")
    name=input()
    browser.get("https://www.instagram.com/explore/tags/"+str(name))
    photo=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div").click()
    time.sleep(5)
    photoin=browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[2]")
    actions=ActionChains(browser)
    actions.double_click(photoin).perform()
if y==5:
    print("enter the Hashtag")
    name=input()
    browser.get("https://www.instagram.com/explore/tags/"+str(name))
    photo=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div").click()
    time.sleep(5)
    photoin=browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea").send_keys("super picture")
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button").click()


    



