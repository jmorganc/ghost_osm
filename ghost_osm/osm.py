"""
TODO:
    -

Endpoints: https://www.openstreetmap.org/user/Obrit/history?list=1
"""

import sys
import requests
import time
import datetime
from bs4 import BeautifulSoup

import config


def main():
    pass


def get_posts():
    url = 'https://www.openstreetmap.org/user/{0}/history?list=1'.format(config.osm['username'])
    page_start = requests.get(url)
    soup = BeautifulSoup(page_start.text)
    # page_start_text = '  <ol class="changesets">    <li data-changeset="{&quot;id&quot;:25738621,&quot;bbox&quot;:{&quot;minlon&quot;:-95.3091191,&quot;minlat&quot;:38.9777067,&quot;maxlon&quot;:-95.2975199,&quot;maxlat&quot;:38.990457}}" id="changeset_25738621">  <h4>    <a class="changeset_id" href="/changeset/25738621">      Added park entry trail and parking lot.    </a>  </h4>  <div class="details">    Closed <abbr title=\'Created: Mon, 29 Sep 2014 05:10:23 +0000&#10;Closed: Mon, 29 Sep 2014 05:10:25 +0000\'>about 2 hours ago</abbr>    &middot;    #25738621  </div></li><li data-changeset="{&quot;id&quot;:25673742,&quot;bbox&quot;:{&quot;minlon&quot;:-96.8866279,&quot;minlat&quot;:29.9003557,&quot;maxlon&quot;:-96.8822618,&quot;maxlat&quot;:29.9028831}}" id="changeset_25673742">  <h4>    <a class="changeset_id" href="/changeset/25673742">      Added parking lot and service road to the slipway.    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Thu, 25 Sep 2014 20:55:24 +0000&#10;Closed: Thu, 25 Sep 2014 20:55:25 +0000>3 days ago</abbr>    &middot;    #25673742  </div></li><li data-changeset="{&quot;id&quot;:25673655,&quot;bbox&quot;:{&quot;minlon&quot;:-96.886664,&quot;minlat&quot;:29.9003096,&quot;maxlon&quot;:-96.8865466,&quot;maxlat&quot;:29.9004458}}" id="changeset_25673655">  <h4>    <a class="changeset_id" href="/changeset/25673655">      Added slipway to the Colorado river.    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Thu, 25 Sep 2014 20:49:58 +0000&#10;Closed: Thu, 25 Sep 2014 20:49:58 +0000>3 days ago</abbr>    &middot;    #25673655  </div></li><li data-changeset="{&quot;id&quot;:25549571,&quot;bbox&quot;:{&quot;minlon&quot;:-96.7374189,&quot;minlat&quot;:32.9520924,&quot;maxlon&quot;:-96.7372561,&quot;maxlat&quot;:32.9522292}}" id="changeset_25549571">  <h4>    <a class="changeset_id" href="/changeset/25549571">      Added the name for the water tower on Lockwood Drive.    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Fri, 19 Sep 2014 20:59:31 +0000&#10;Closed: Fri, 19 Sep 2014 20:59:32 +0000>9 days ago</abbr>    &middot;    #25549571  </div></li><li data-changeset="{&quot;id&quot;:24431416,&quot;bbox&quot;:{&quot;minlon&quot;:-96.7491028,&quot;minlat&quot;:32.9537925,&quot;maxlon&quot;:-96.7439433,&quot;maxlat&quot;:32.9564235}}" id="changeset_24431416">  <h4>    <a class="changeset_id" href="/changeset/24431416">      Added sidewalk.    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Tue, 29 Jul 2014 20:52:45 +0000&#10;Closed: Tue, 29 Jul 2014 20:52:46 +0000>2 months ago</abbr>    &middot;    #24431416  </div></li><li data-changeset="{&quot;id&quot;:24338189,&quot;bbox&quot;:{&quot;minlon&quot;:-95.2113213,&quot;minlat&quot;:30.0591072,&quot;maxlon&quot;:-95.2103463,&quot;maxlat&quot;:30.0595959}}" id="changeset_24338189">  <h4>    <a class="changeset_id" href="/changeset/24338189">      Moved Kingwood First Baptist Church to the proper side of the road.    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Thu, 24 Jul 2014 21:02:08 +0000&#10;Closed: Thu, 24 Jul 2014 21:02:08 +0000>2 months ago</abbr>    &middot;    #24338189  </div></li><li data-changeset="{&quot;id&quot;:24338107,&quot;bbox&quot;:{&quot;minlon&quot;:-95.1891476,&quot;minlat&quot;:30.0594528,&quot;maxlon&quot;:-95.1879823,&quot;maxlat&quot;:30.0597084}}" id="changeset_24338107">  <h4>    <a class="changeset_id" href="/changeset/24338107">      Creekwood Middle School bicycle parking.    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Thu, 24 Jul 2014 20:57:08 +0000&#10;Closed: Thu, 24 Jul 2014 20:57:09 +0000>2 months ago</abbr>    &middot;    #24338107  </div></li><li data-changeset="{&quot;id&quot;:24337771,&quot;bbox&quot;:{&quot;minlon&quot;:-96.7747828,&quot;minlat&quot;:33.8154435,&quot;maxlon&quot;:-96.7692068,&quot;maxlat&quot;:33.8195667}}" id="changeset_24337771">  <h4>    <a class="changeset_id" href="/changeset/24337771">      Mill Creek Resort and Marina.    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Thu, 24 Jul 2014 20:35:41 +0000&#10;Closed: Thu, 24 Jul 2014 20:35:42 +0000>2 months ago</abbr>    &middot;    #24337771  </div></li><li data-changeset="{&quot;id&quot;:24337755,&quot;bbox&quot;:{&quot;minlon&quot;:-96.7724695,&quot;minlat&quot;:33.8176197,&quot;maxlon&quot;:-96.7714391,&quot;maxlat&quot;:33.8186532}}" id="changeset_24337755">  <h4>    <a class="changeset_id" href="/changeset/24337755">      Mill Creek Marina car parking.    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Thu, 24 Jul 2014 20:34:17 +0000&#10;Closed: Thu, 24 Jul 2014 20:34:18 +0000>2 months ago</abbr>    &middot;    #24337755  </div></li><li data-changeset="{&quot;id&quot;:24337737,&quot;bbox&quot;:{&quot;minlon&quot;:-96.7708181,&quot;minlat&quot;:33.8185504,&quot;maxlon&quot;:-96.7684123,&quot;maxlat&quot;:33.8189593}}" id="changeset_24337737">  <h4>    <a class="changeset_id" href="/changeset/24337737">      Mill Creek Marina breakwater.    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Thu, 24 Jul 2014 20:33:23 +0000&#10;Closed: Thu, 24 Jul 2014 20:33:23 +0000>2 months ago</abbr>    &middot;    #24337737  </div></li><li data-changeset="{&quot;id&quot;:22560496,&quot;bbox&quot;:{&quot;minlon&quot;:-5.8935982,&quot;minlat&quot;:57.0647881,&quot;maxlon&quot;:-5.8934627,&quot;maxlat&quot;:57.0648903}}" id="changeset_22560496">  <h4>    <a class="changeset_id" href="/changeset/22560496">      Seafari is now Isle of Skye Leather Shop on the Armadale pier.    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Mon, 26 May 2014 11:07:36 +0000&#10;Closed: Mon, 26 May 2014 11:07:37 +0000>4 months ago</abbr>    &middot;    #22560496  </div></li><li data-changeset="{&quot;id&quot;:22560445,&quot;bbox&quot;:{&quot;minlon&quot;:-6.5863841,&quot;minlat&quot;:57.4473676,&quot;maxlon&quot;:-6.5860682,&quot;maxlat&quot;:57.4475809}}" id="changeset_22560445">  <h4>    <a class="changeset_id" href="/changeset/22560445">      Removed cafe point and added building for MacLeod Tables Cafe.    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Mon, 26 May 2014 11:04:33 +0000&#10;Closed: Mon, 26 May 2014 11:04:34 +0000>4 months ago</abbr>    &middot;    #22560445  </div></li><li data-changeset="{&quot;id&quot;:22560257,&quot;bbox&quot;:{&quot;minlon&quot;:-6.1758803,&quot;minlat&quot;:57.4946466,&quot;maxlon&quot;:-6.1579015,&quot;maxlat&quot;:57.504363}}" id="changeset_22560257">  <h4>    <a class="changeset_id" href="/changeset/22560257">      Added a note to the forest at the base of the Storr indicating it has recently been felled.    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Mon, 26 May 2014 10:53:52 +0000&#10;Closed: Mon, 26 May 2014 10:53:57 +0000>4 months ago</abbr>    &middot;    #22560257  </div></li><li data-changeset="{&quot;id&quot;:22560165,&quot;bbox&quot;:{&quot;minlon&quot;:-4.2328751,&quot;minlat&quot;:57.4746177,&quot;maxlon&quot;:-4.2322414,&quot;maxlat&quot;:57.4748831}}" id="changeset_22560165">  <h4>    <a class="changeset_id" href="/changeset/22560165">      Added Glencairn and Ardross Guest Houses in Inverness.    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Mon, 26 May 2014 10:48:06 +0000&#10;Closed: Mon, 26 May 2014 10:48:07 +0000>4 months ago</abbr>    &middot;    #22560165  </div></li><li data-changeset="{&quot;id&quot;:22323997,&quot;bbox&quot;:{&quot;minlon&quot;:-117.220598,&quot;minlat&quot;:32.7284723,&quot;maxlon&quot;:-117.2195211,&quot;maxlat&quot;:32.7300334}}" id="changeset_22323997">  <h4>    <a class="changeset_id" href="/changeset/22323997">      (no comment)    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Wed, 14 May 2014 00:23:42 +0000&#10;Closed: Wed, 14 May 2014 00:23:43 +0000>5 months ago</abbr>    &middot;    #22323997  </div></li><li data-changeset="{&quot;id&quot;:22323929,&quot;bbox&quot;:{&quot;minlon&quot;:-64.7518236,&quot;minlat&quot;:18.4263572,&quot;maxlon&quot;:-64.4361205,&quot;maxlat&quot;:18.4506283}}" id="changeset_22323929">  <h4>    <a class="changeset_id" href="/changeset/22323929">      (no comment)    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Wed, 14 May 2014 00:11:19 +0000&#10;Closed: Wed, 14 May 2014 00:11:21 +0000>5 months ago</abbr>    &middot;    #22323929  </div></li><li data-changeset="{&quot;id&quot;:22323823,&quot;bbox&quot;:{&quot;minlon&quot;:-85.1508569,&quot;minlat&quot;:9.6000009,&quot;maxlon&quot;:-85.1322726,&quot;maxlat&quot;:9.6293902}}" id="changeset_22323823">  <h4>    <a class="changeset_id" href="/changeset/22323823">      Casa Chameleon.    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Tue, 13 May 2014 23:56:06 +0000&#10;Closed: Tue, 13 May 2014 23:56:08 +0000>5 months ago</abbr>    &middot;    #22323823  </div></li><li data-changeset="{&quot;id&quot;:22323808,&quot;bbox&quot;:{&quot;minlon&quot;:-85.1121178,&quot;minlat&quot;:9.5663226,&quot;maxlon&quot;:-85.1003623,&quot;maxlat&quot;:9.5838403}}" id="changeset_22323808">  <h4>    <a class="changeset_id" href="/changeset/22323808">      Extended Cabo Blanco trail down to the beach.    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Tue, 13 May 2014 23:53:34 +0000&#10;Closed: Tue, 13 May 2014 23:53:35 +0000>5 months ago</abbr>    &middot;    #22323808  </div></li><li data-changeset="{&quot;id&quot;:22323781,&quot;bbox&quot;:{&quot;minlon&quot;:-97.8141706,&quot;minlat&quot;:32.2489282,&quot;maxlon&quot;:-97.809788,&quot;maxlat&quot;:32.2502782}}" id="changeset_22323781">  <h4>    <a class="changeset_id" href="/changeset/22323781">      (no comment)    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Tue, 13 May 2014 23:48:58 +0000&#10;Closed: Tue, 13 May 2014 23:48:59 +0000>5 months ago</abbr>    &middot;    #22323781  </div></li><li data-changeset="{&quot;id&quot;:22323673,&quot;bbox&quot;:{&quot;minlon&quot;:-95.6173473,&quot;minlat&quot;:33.8626864,&quot;maxlon&quot;:-95.5024097,&quot;maxlat&quot;:33.8734349}}" id="changeset_22323673">  <h4>    <a class="changeset_id" href="/changeset/22323673">      Forest Chapel church building, parking lot and service road.    </a>  </h4>  <div class="details">    Closed <abbr title=Created: Tue, 13 May 2014 23:37:16 +0000&#10;Closed: Tue, 13 May 2014 23:37:19 +0000>5 months ago</abbr>    &middot;    #22323673  </div></li>  </ol>  <div class="changeset_more">    <a class="button load_more" href="/user/Obrit/history?list=1&amp;max_id=22323672">Load more</a>    <img alt="Searching" class="loader" src="/assets/searching-afa9db3d84314271544c01b59999b264.gif" style="display: none;" />  </div>'
    # soup = BeautifulSoup(page_start_text)

    posts = []

    """
    If ol.changesets, there are changes.
    If div.changeset_more, there are more changes.
    If neither, there are no (more) changes.
    """
    while True:
        ol_changesets = soup.find('ol', class_='changesets')
        a_load_more = soup.find('a', class_='load_more')
        if ol_changesets:
            for li in ol_changesets.select('li'):
                description =  li.h4.a.contents[0].strip()
                date_created = li.div.abbr['title'].replace('Created:', '|').replace('Closed:', '|').split('|')[1].strip()
                #Wed, 14 Aug 2014 HH:MM:SS +0000
                #print date_created
                date_created = time.strptime(date_created, '%a, %d %b %Y %H:%M:%S +0000')
                #Ghost format: 2014-04-15T12:36:28.353Z
                datetime_formatted = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', date_created)
                #print date_created
                #print time.gmtime()
                #date_created_datetime = datetime.datetime.fromtimestamp(time.mktime(date_created))
                #print date_created_datetime
                #date_created_utc = date_created_datetime.utcnow()
                #print date_created_utc
                #print time.strftime('%Y-%m-%d %H:%M:%S', date_created)
                #print datetime.tzinfo.fromutc(date_created_utc)
                posts.append({
                    'created': datetime_formatted,
                    'description': description
                })
            if a_load_more:
                #break
                url = 'https://www.openstreetmap.org{0}'.format(a_load_more['href'])
                page = requests.get(url)
                soup = BeautifulSoup(page.text)
            else:
                break
        else:
            break

    return posts


if __name__ == '__main__':
    sys.exit(main())
