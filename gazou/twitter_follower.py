#ライブラリのインポート
import tweepy
#Twitterの認証

from django.shortcuts import render
from .forms import GazouForm

def twifow(request):

    params = {
        'title': 'Hello',
        'temp_list':"",
        'form': GazouForm()
    }

    if (request.method == 'POST'):#入力があるかどうか
        CK='*'
        CS='*'
        AT='*'
        AS='*'

        # Twitterオブジェクトの生成
        auth = tweepy.OAuthHandler(CK, CS)
        auth.set_access_token(AT, AS)

        api = tweepy.API(auth)

        searchname=request.POST['name'] #ユーザーIDを入れる。
        fl_count=int(request.POST['fl']) #最低フォロワー数を入れる
        header_point=(request.POST['word']) #界隈名を入れる

        friends_ids = [] #対象ユーザーがフォローしている人を入れる箱
        Big_friends_ids= [] #friend_idsの中のユーザーからフォロワーが多い人を入れる箱
        fl_name=[] #有名人ユーザーの名前
        backimage=[] #有名人ユーザーのプロフィール画像
        flcount=[] #有名人ユーザーのフォロワー数。
        diss=[] #有名人ユーザーのツイッタープロフィール
        friend_count=[] #有名人ユーザーのフォロー数
        sc_name=[] #有名人ユーザーのユーザーID

        # フォローした人のIDを全取得
        # Cursor使うとすべて取ってきてくれるが，配列ではなくなるので配列に入れる
        try:
            for friend_id in tweepy.Cursor(api.get_friend_ids, screen_name=searchname).items():#指定したユーザーがフォローしている人を順に取り出す。
                friends_ids.append(friend_id)
            for i in range(0, len(friends_ids), 100):
                for user in api.lookup_users(user_id=friends_ids[i:i+100]):
                    if user.followers_count > fl_count and header_point in user.description: #フォロワーが多い人だけ選出。
                        Big_friends_ids.append("https://twitter.com/{}".format(user.screen_name))
                        fl_name.append(user.name)
                        backimage.append(user.profile_image_url_https)
                        flcount.append(user.followers_count)
                        diss.append(user.description)
                        friend_count.append(user.friends_count)
                        sc_name.append(user.screen_name)

            temp_list = []
            for i, _ in enumerate(Big_friends_ids):
                temp_list.append({
                    'URL': Big_friends_ids[i],
                    'namename': fl_name[i],
                    'backimage':backimage[i],
                    'flcount':flcount[i],
                    'diss':diss[i],
                    'friend':friend_count[i],
                    'sc':sc_name[i],
            })              
            
            params['temp_list'] = temp_list
            params['form'] = GazouForm(request.POST)
        
        except tweepy.errors.NotFound:
            return render(request, 'gazou/except.html', params) #ユーザーIDが間違っていた場合

        except tweepy.errors.TweepyException:
            return render(request,'gazou/exceptall.html',params) #tweepyエラー全般が起きた場合。

        return render(request, 'gazou/hometown.html', params) #正常な場合

    else:
        return render(request, 'gazou/home.html', params) #フォームに入力せずにここに辿り着いた場合
