"""Builds every page of live-sub.com in Korean (/) and English (/en/).

Run from the repo root:  python scripts/build.py
Edit the data below, rebuild, commit the generated HTML.
"""
import json, os, datetime

SITE = 'https://live-sub.com'
CSS_V = 'r3'
TODAY = datetime.date.today().isoformat()
BOT_RE = 'bot|crawl|spider|slurp|google|bing|naver|yeti|daum|lighthouse|facebookexternalhit'

# ---------------------------------------------------------------- family sites
SITES = [  # key, ko name, en name, url, ko desc, en desc, domain suffix, chips ko, chips en
    ('trans', 'Transtream', 'Transtream', 'https://transtream.app/', '라이브 방송·화상통화 실시간 자막 번역', 'Real-time captions and translation for live streams and calls', '.app', [], []),
    ('health', '헬띠루틴', 'Healthy Routine', '/healthyroutine/', '운동 기록과 루틴 관리를 한 앱에서. 꾸준함을 습관으로.', 'Workout logs and routine management in one simple app.', 'app', ['운동 기록', '루틴'], ['Workout log', 'Routines']),
    ('hongbo', '더홍보', 'THE HONGBO', 'https://thehongbo.com/', '앱·상품·서비스 누구나 자유롭게 알리는 홍보 플랫폼.', 'A platform for anyone to promote apps, products and services.', '.com', ['홍보', '발견'], ['Promotion', 'Discovery']),
    ('ssrrr', 'SSRRR', 'SSRRR', 'https://ssrrr.net/', '유머부터 이슈·경제까지, 스르륵 가볍게 보는 커뮤니티.', 'Humor, issues and economy — a light content community.', '.net', ['유머', '이슈'], ['Humor', 'Issues']),
    ('matda', '맡다', 'MATDA', 'https://matda.net/', '일을 올리고 업체·전문가 견적을 비교하는 업무 매칭.', 'Post a job and compare quotes from companies and experts.', '.net', ['견적 비교', 'B2B'], ['Quotes', 'B2B']),
    ('tool', 'manytool', 'manytool', 'https://manytool.net/', 'FPS 감도, 롤 챔프, 컬러 추천 — 작지만 유용한 도구 모음.', 'FPS sensitivity, LoL champs, color picks — small, useful tools.', '.net', ['FPS 감도', '컬러'], ['FPS', 'Color']),
    ('hire', 'hireroom', 'hireroom', 'https://hireroom.net/', '중소기업도 쉽게 만드는 우리 회사만의 채용 페이지.', 'Career pages any small business can build in minutes.', '.net', ['채용 페이지', 'HR'], ['Careers', 'HR']),
]
ALT = {'Transtream': '트랜스트림', '헬띠루틴': 'Healthy Routine', 'Healthy Routine': '헬띠루틴', '더홍보': 'THE HONGBO', 'THE HONGBO': '더홍보', 'SSRRR': '스르륵', '맡다': 'MATDA', 'MATDA': '맡다', 'manytool': '매니툴', 'hireroom': '하이어룸'}

# ---------------------------------------------------------------- guides
# slug, kind, ko name, en name, ko search phrase, ko intro, en intro, ko tips, en tips
GUIDES = [
    ('chzzk', 'stream', '치지직', 'CHZZK', '치지직 번역 · 실시간 자막',
     '해외 시청자와 함께하는 치지직 방송, 혹은 외국어로 진행되는 치지직 방송을 볼 때 Transtream으로 방송 음성을 실시간 자막으로 바꿔 볼 수 있습니다.',
     'Watching a CHZZK stream in a language you don’t speak? Transtream turns the stream audio into real-time subtitles in your language.',
     ['채팅창을 접어두면 자막 패널을 놓을 공간이 넓어집니다.', '게임 효과음이 큰 방송은 방송 볼륨을 적당히 맞추면 인식이 더 안정적입니다.'],
     ['Collapse the chat panel to make room for the subtitle panel.', 'For loud game streams, a moderate stream volume keeps recognition stable.']),
    ('soop', 'stream', 'SOOP(아프리카TV)', 'SOOP (AfreecaTV)', 'SOOP·아프리카TV 번역 · 실시간 자막',
     'SOOP(구 아프리카TV)의 해외 BJ 방송이나 글로벌 방송을 볼 때, 브라우저에서 재생되는 음성을 Transtream이 실시간 자막으로 번역합니다.',
     'Follow SOOP (formerly AfreecaTV) streams across languages — Transtream translates the browser audio into live subtitles.',
     ['플레이어를 브라우저 전체 화면 대신 넓은 창으로 두면 자막 패널과 함께 보기 편합니다.', '여러 방송을 동시에 열었다면 자막을 볼 방송 탭 하나만 선택하세요.'],
     ['Use a wide window instead of fullscreen so the subtitle panel sits beside the player.', 'If several streams are open, select only the tab you want subtitled.']),
    ('youtube', 'stream', '유튜브 라이브', 'YouTube Live', '유튜브 라이브 실시간 번역 · 자막',
     '자동 자막이 없거나 번역이 늦는 유튜브 라이브도 Transtream으로 실시간 번역 자막을 띄워 볼 수 있습니다. 해외 컨퍼런스, 뉴스 생중계, 해외 크리에이터 라이브에 유용합니다.',
     'Many YouTube Live streams have no live captions or translation. Transtream adds real-time translated subtitles for conferences, news and creator streams.',
     ['유튜브 자체 자막(CC)은 꺼 두면 화면이 겹치지 않습니다.', '재생 속도는 1배속으로 두는 것이 가장 정확합니다.'],
     ['Turn off YouTube’s own CC so captions don’t overlap.', 'Keep playback at 1x speed for the best accuracy.']),
    ('twitch', 'stream', '트위치', 'Twitch', '트위치 번역 · 실시간 자막',
     '해외 트위치 스트리머의 방송을 실시간 자막으로 따라가 보세요. Transtream이 방송 음성을 원하는 언어로 번역해 보여 줍니다.',
     'Follow Twitch streamers in any language — Transtream translates the stream audio into real-time subtitles.',
     ['극장 모드(Theater mode)를 쓰면 화면 배치가 깔끔합니다.', '광고가 재생되는 동안에는 자막이 잠시 멈출 수 있습니다.'],
     ['Theater mode gives a clean layout next to the subtitles.', 'Captions may pause while an ad is playing.']),
    ('tiktok', 'stream', '틱톡 라이브', 'TikTok LIVE', '틱톡 라이브 번역 · 실시간 자막',
     'PC 브라우저에서 보는 틱톡 라이브의 음성을 Transtream으로 실시간 자막 번역할 수 있습니다. 해외 라이브 커머스나 크리에이터 방송을 볼 때 유용합니다.',
     'Watch TikTok LIVE in a desktop browser and let Transtream translate the audio into readable subtitles.',
     ['모바일 앱이 아닌 PC 브라우저의 tiktok.com 라이브에서 사용하세요.', '세로 화면 방송은 창 옆에 자막 패널을 두면 보기 좋습니다.'],
     ['Use TikTok LIVE on tiktok.com in a desktop browser, not the mobile app.', 'Vertical streams fit nicely with the subtitle panel beside them.']),
    ('japanese', 'stream', '일본 방송·버튜버', 'Japanese streams & VTubers', '일본 방송 · 버튜버 실시간 번역',
     '홀로라이브·니지산지 같은 일본 버튜버 방송이나 일본어 라이브를 볼 때, Transtream으로 일본어 음성을 한국어 자막으로 실시간 번역해 볼 수 있습니다.',
     'Watch Japanese streams and VTubers with real-time translated subtitles — Transtream turns Japanese speech into your language.',
     ['음성 언어를 일본어로, 자막 언어를 한국어로 지정하세요.', '노래 방송(우타와꾸)보다 잡담 방송에서 정확도가 높습니다.'],
     ['Set the spoken language to Japanese and the subtitle language to yours.', 'Talk streams translate more accurately than singing streams.']),
    ('zoom', 'meeting', '줌(Zoom) 회의', 'Zoom meetings', '줌 회의 실시간 번역 · 자막',
     '해외 거래처나 글로벌 팀과의 줌 회의에서 상대의 말을 실시간 번역 자막으로 확인하세요. 브라우저에서 참여한 줌 회의의 음성을 Transtream이 번역합니다.',
     'Read real-time translated captions of what others say in your Zoom meetings with global partners and teams.',
     ['데스크톱 앱 대신 브라우저로 회의에 참여하면 탭 오디오를 바로 선택할 수 있습니다.', '회의 녹음·번역 전에 참석자에게 미리 알리는 것이 좋습니다.'],
     ['Join from the browser instead of the desktop app so you can select the tab audio.', 'Let participants know you are using live translation.']),
    ('google-meet', 'meeting', '구글 미트', 'Google Meet', '구글 미트 실시간 번역 · 자막',
     '구글 미트 화상회의에서 외국어로 말하는 참석자의 음성을 Transtream으로 실시간 번역 자막으로 볼 수 있습니다.',
     'See real-time translated captions of other participants in Google Meet calls.',
     ['구글 미트 자체 자막은 꺼 두면 화면이 겹치지 않습니다.', '발언자가 마이크에 가까울수록 번역이 정확해집니다.'],
     ['Turn off Meet’s built-in captions to avoid overlap.', 'Clear speaker audio means more accurate translation.']),
    ('discord', 'meeting', '디스코드', 'Discord', '디스코드 통화 번역 · 실시간 자막',
     '해외 친구들과의 디스코드 음성 채널이나 게임 중 통화를 Transtream 실시간 번역 자막으로 따라가 보세요. 브라우저 버전 디스코드에서 사용하기 가장 쉽습니다.',
     'Follow Discord voice channels with friends abroad using Transtream’s real-time translated captions — easiest with Discord in the browser.',
     ['discord.com 웹 버전으로 접속하면 탭 오디오를 선택할 수 있습니다.', '여러 명이 동시에 말하면 번역이 섞일 수 있습니다.'],
     ['Use Discord on discord.com so the tab audio can be selected.', 'Overlapping speakers can mix up the translation.']),
    ('stripchat', 'stream', 'Stripchat', 'Stripchat', 'Stripchat 번역 · 실시간 자막',
     'Stripchat 방송을 브라우저에서 볼 때 방송 음성을 Transtream 실시간 자막으로 번역하는 방법입니다.',
     'How to translate Stripchat browser audio into real-time subtitles with Transtream.', [], []),
    ('chaturbate', 'stream', 'Chaturbate', 'Chaturbate', 'Chaturbate 번역 · 실시간 자막',
     'Chaturbate 방송을 브라우저에서 볼 때 방송 음성을 Transtream 실시간 자막으로 번역하는 방법입니다.',
     'How to translate Chaturbate browser audio into real-time subtitles with Transtream.', [], []),
]

# ---------------------------------------------------------------- UI copy
L = {
 'ko': dict(prefix='', other='en', otherlabel='EN', otherfull='English',
  nav=['Transtream', '패밀리 사이트', '플랫폼 가이드'], open='Transtream 열기', start='Transtream 시작하기',
  ann='광고 · 브랜드 제휴 · 콘텐츠 협업 문의', annb='제휴 모집 중',
  fdesc='live sub는 언어, 일, 생활을 잇는 작은 서비스들을 만드는 팀입니다.', fh=['패밀리 사이트', '바로가기'], contact='제휴 문의',
  home_title='live sub | 트랜스트림·헬띠루틴·더홍보·SSRRR·맡다 패밀리 사이트',
  home_desc='live sub 패밀리 사이트 — 트랜스트림(Transtream) 실시간 자막 번역, 헬띠루틴 운동 기록 앱, 더홍보 홍보 플랫폼, SSRRR 커뮤니티, 맡다 견적 매칭, 매니툴, 하이어룸을 한곳에서.',
  pill='실시간 AI 통역', h1='언어는 달라도,<br><span class="grad">순간은 같게.</span>',
  lede='라이브 방송, 글로벌 미팅, 화상통화. Transtream이 들리는 말을 실시간 자막과 번역으로 바꿔 드립니다.',
  cta2='패밀리 사이트 보기', src='Good morning everyone, today we have something new to share.',
  caps=[('KO', '좋은 아침이에요 여러분, 오늘은 새로운 소식을 전해드릴게요.'), ('JA', '皆さんおはようございます。今日は新しいお知らせがあります。'), ('ES', 'Buenos días a todos, hoy tenemos algo nuevo que compartir.')],
  f1=('AI TRANSLATION', '실시간 번역'), f2=('LANGUAGES', '40+ 언어 지원'), viewers='2,482명 시청 중',
  plat='브라우저에서 보는 라이브와 회의 어디서나',
  howE='How it works', howH='세 단계면 <span>충분합니다.</span>', howS='보고 있는 라이브나 회의 탭을 연결하면 바로 자막이 나옵니다.',
  steps=[('◉', '연결', '보고 싶은 라이브나 미팅 탭의 오디오를 Transtream에 연결하세요.'), ('≋', '이해', '실시간 자막과 번역이 대화의 흐름을 놓치지 않게 따라갑니다.'), ('↗', '확장', '언어 걱정 없이 더 많은 사람, 더 넓은 세계와 만나세요.')],
  famE='live sub family', famH='하나의 팀, <span>일곱 개의 서비스.</span>', famS='라이브를 넘어 일과 생활의 다음 장면까지. 필요한 순간에 꼭 필요한 서비스를 만듭니다.',
  trans_desc='라이브 방송과 화상통화를 위한 실시간 자막·번역. 치지직, SOOP, 유튜브, 트위치, 줌 어디서든.', trans_chips=['실시간 자막', '40+ 언어', '브라우저'],
  gE='Platform guides', gH='플랫폼별 <span>번역 가이드.</span>', gAll='전체 가이드',
  fin='지금 보는 라이브,<br>당신의 언어로.', finS='브라우저만 있으면 바로 시작할 수 있습니다.',
  # guides
  g_title='플랫폼별 실시간 번역 가이드 | 치지직·유튜브·트위치·줌 | live sub',
  g_desc='치지직, SOOP(아프리카TV), 유튜브 라이브, 트위치, 틱톡, 줌, 구글 미트, 디스코드 방송과 회의를 Transtream으로 실시간 번역 자막과 함께 보는 방법.',
  g_h1='라이브와 회의를<br><span class="grad">내 언어로.</span>', g_lede='자주 쓰는 플랫폼에서 Transtream 실시간 번역 자막을 켜는 방법을 플랫폼별로 정리했습니다.',
  g_streams='라이브 방송', g_meetings='회의 · 통화',
  g_note='각 가이드는 독립적인 번역 도구의 사용 안내입니다. live sub와 Transtream은 언급된 플랫폼과 제휴하거나 승인받지 않았습니다.',
  gp_title=lambda g: f'{g[4]} 방법 | Transtream 가이드',
  gp_desc=lambda g: f'{g[2]} {"방송" if g[1]=="stream" else ""}을 실시간 번역 자막으로 보는 방법. Transtream으로 {g[2]} 음성을 한국어·영어·일본어 등 원하는 언어 자막으로 번역하세요.'.replace('  ', ' '),
  gp_h1=lambda g: f'{g[2]} 실시간 번역 자막 켜는 법', back='← 플랫폼 가이드',
  need='준비물', setup='설정 방법', tips='더 잘 쓰는 팁', trouble='자막이 나오지 않을 때', faq='자주 묻는 질문', related='다른 가이드',
  needs=lambda g: [f'{g[2]}{"을" if g[1]=="meeting" else ""} 연 PC(데스크톱) 브라우저 탭', '다른 탭이나 창에서 연 Transtream', '번역해서 볼 자막 언어'],
  steps_g=lambda g: [f'PC 브라우저에서 {g[2]} {"방송" if g[1]=="stream" else "회의"}을 엽니다.', 'Transtream을 열고 번역 세션을 시작합니다.', f'오디오 소스로 {g[2]} 탭(또는 시스템 오디오)을 선택합니다.', '말하는 언어와 자막 언어를 고릅니다.', '자막 패널을 플레이어나 화면을 가리지 않는 위치에 둡니다.'],
  trouble_t='선택한 탭에서 실제로 소리가 나는지, 탭이 음소거되어 있지 않은지, 브라우저의 오디오 공유 권한이 켜져 있는지 확인하세요. 탭을 새로 열었다면 오디오 소스를 다시 연결해야 합니다.',
  faqs=lambda g: [(f'{g[2]} 번역은 앱 설치가 필요한가요?', '아니요. Transtream은 브라우저에서 동작하며, PC 브라우저에서 재생 중인 탭의 오디오를 선택해 사용합니다.'),
                  (f'{g[2]} 음성을 녹화하거나 저장하나요?', 'Transtream은 세션에 공유된 오디오를 번역 자막으로 보여 줄 뿐, 방송이나 회의를 녹화·다운로드·재배포하지 않습니다.'),
                  ('어떤 언어로 번역할 수 있나요?', '한국어, 영어, 일본어, 스페인어 등 40개 이상의 언어를 지원합니다. 말하는 언어와 자막 언어를 각각 선택할 수 있습니다.')],
  notice=lambda g: f'{g[2]}은(는) 해당 소유자의 상표입니다. Transtream과 live sub는 {g[2]}와 제휴하거나 승인받은 서비스가 아닙니다.',
  # healthy routine
  hr_title='헬띠루틴 | 운동 기록·루틴 관리 앱 (Healthy Routine)',
  hr_desc='헬띠루틴(Healthy Routine) — 운동 기록, 운동 루틴 관리, 헬스 일지를 한곳에서. Google Play에서 다운로드하세요.',
  hr_name='헬띠루틴', hr_h1='운동을<br><span class="grad">습관으로.</span>', hr_lede='운동 기록과 루틴 관리를 한곳에서. 오늘의 운동을 남기고, 나만의 루틴을 꾸준히 이어가세요.',
  hr_dl='Google Play에서 다운로드', hr_f=[('TRACK', '운동 기록', '오늘 어떤 운동을 했는지 간단하게 기록하고 나의 변화를 확인하세요.'), ('ROUTINE', '루틴 관리', '반복하고 싶은 운동 루틴을 정리해 다음 운동을 더 쉽게 시작하세요.'), ('HABIT', '꾸준한 습관', '작은 기록을 쌓아 운동을 일상의 자연스러운 습관으로 만들어보세요.')],
  hr_note='헬띠루틴은 운동 관리, 운동 기록, 루틴 관리를 위한 앱입니다. 자세한 앱 정보는 Google Play에서 확인할 수 있습니다.',
 ),
 'en': dict(prefix='/en', other='ko', otherlabel='KO', otherfull='한국어',
  nav=['Transtream', 'Family sites', 'Platform guides'], open='Open Transtream', start='Start Transtream',
  ann='Advertising · brand partnerships · content collaboration', annb='Partnerships open',
  fdesc='live sub is a small team building services that connect language, work and life.', fh=['Family sites', 'Links'], contact='Partnerships',
  home_title='live sub | Transtream, Healthy Routine, THE HONGBO, SSRRR & MATDA',
  home_desc='live sub family sites: Transtream real-time live stream translation, Healthy Routine workout tracker, THE HONGBO promotion platform, SSRRR community, MATDA quote matching, manytool and hireroom.',
  pill='Real-time AI interpretation', h1='Different language.<br><span class="grad">Same moment.</span>',
  lede='Live streams, global meetings, video calls. Transtream turns what you hear into real-time captions and translation.',
  cta2='Explore family sites', src='좋은 아침이에요 여러분, 오늘은 새로운 소식을 전해드릴게요.',
  caps=[('EN', 'Good morning everyone, today we have something new to share.'), ('JA', '皆さんおはようございます。今日は新しいお知らせがあります。'), ('ES', 'Buenos días a todos, hoy tenemos algo nuevo que compartir.')],
  f1=('AI TRANSLATION', 'Real-time'), f2=('LANGUAGES', '40+ supported'), viewers='2,482 watching',
  plat='Works with live streams and meetings in your browser',
  howE='How it works', howH='Three steps. <span>That’s it.</span>', howS='Connect the stream or meeting tab you’re on and captions appear.',
  steps=[('◉', 'Connect', 'Point Transtream at the audio of the live stream or meeting tab.'), ('≋', 'Understand', 'Real-time captions and translation keep up with every line.'), ('↗', 'Go further', 'Meet more people across the world without the language barrier.')],
  famE='live sub family', famH='One team. <span>Seven useful worlds.</span>', famS='Beyond live streams — services for the next moments of work and everyday life.',
  trans_desc='Real-time captions and translation for live streams and video calls — YouTube, Twitch, CHZZK, SOOP, Zoom and more.', trans_chips=['Live captions', '40+ languages', 'Browser'],
  gE='Platform guides', gH='Translation guides <span>by platform.</span>', gAll='All guides',
  fin='The stream you’re watching,<br>in your language.', finS='All you need is a browser.',
  g_title='Live Translation Guides for YouTube, Twitch, Zoom & more | live sub',
  g_desc='How to watch YouTube Live, Twitch, CHZZK, SOOP, TikTok LIVE, Zoom, Google Meet and Discord with real-time translated subtitles using Transtream.',
  g_h1='Streams and meetings,<br><span class="grad">in your language.</span>', g_lede='Step-by-step guides for turning on Transtream’s real-time translated captions where you already watch and talk.',
  g_streams='Live streams', g_meetings='Meetings & calls',
  g_note='These are setup guides for an independent translation tool. live sub and Transtream are not affiliated with or endorsed by the platforms mentioned.',
  gp_title=lambda g: f'How to Translate {g[3]} in Real Time | Transtream guide',
  gp_desc=lambda g: f'Watch {g[3]} with real-time translated subtitles. Transtream translates {g[3]} audio into English, Korean, Japanese and 40+ languages.',
  gp_h1=lambda g: f'How to translate {g[3]} in real time', back='← Platform guides',
  need='What you need', setup='Setup steps', tips='Tips', trouble='If captions don’t appear', faq='FAQ', related='More guides',
  needs=lambda g: [f'{g[3]} open in a desktop browser tab', 'Transtream open in another tab or window', 'Your preferred subtitle language'],
  steps_g=lambda g: [f'Open {g[3]} in a desktop browser.', 'Open Transtream and start a translation session.', f'Select the {g[3]} tab (or system audio) as the audio source.', 'Choose the spoken language and the subtitle language.', 'Place the subtitle panel where it doesn’t cover the player.'],
  trouble_t='Check that the selected tab is actually playing sound, isn’t muted, and that browser audio sharing permission is on. If you reopened the tab, reconnect the audio source.',
  faqs=lambda g: [(f'Do I need to install an app to translate {g[3]}?', 'No. Transtream runs in the browser and uses the audio of the tab you select.'),
                  (f'Does Transtream record {g[3]}?', 'No. It only shows translated captions for the audio shared with the session — it does not record, download or redistribute anything.'),
                  ('Which languages are supported?', 'More than 40, including English, Korean, Japanese and Spanish. You choose the spoken and subtitle languages separately.')],
  notice=lambda g: f'{g[3]} is a trademark of its respective owner. Transtream and live sub are independent and not affiliated with or endorsed by {g[3]}.',
  hr_title='Healthy Routine | Workout Tracker & Routine Planner App',
  hr_desc='Healthy Routine (헬띠루틴) — log workouts, manage routines and build habits. Get it on Google Play.',
  hr_name='Healthy Routine', hr_h1='Make movement<br><span class="grad">a habit.</span>', hr_lede='Track your workouts and manage your routines in one simple place. Record today’s movement and keep building your routine.',
  hr_dl='Get it on Google Play', hr_f=[('TRACK', 'Workout records', 'Keep a simple record of what you did today and see your progress over time.'), ('ROUTINE', 'Routine management', 'Organize the routines you want to repeat so your next workout is easier to start.'), ('HABIT', 'Build consistency', 'Turn small records into a natural, sustainable part of everyday life.')],
  hr_note='Healthy Routine is an app for workout management, exercise records and routine planning. See Google Play for details.',
 ),
}
PLAY = 'https://play.google.com/store/apps/details?id=com.healthyroutine.app'


def url(lang, path):  # path like '/guides/'
    return (L[lang]['prefix'] + path) if path.startswith('/') else path


def ext(href):
    return ' target="_blank" rel="noopener"' if href.startswith('http') else ''


def sname(s, lang):
    return s[1] if lang == 'ko' else s[2]


def lang_script(lang, other_path):
    # Korean browsers get /, everyone else /en/ — unless they picked a language or are a crawler.
    want = 'ko' if lang == 'en' else 'en'
    cond = "l.indexOf('ko')===0" if lang == 'en' else "l&&l.indexOf('ko')!==0"
    return ('<script>document.documentElement.classList.add("js");(function(){try{var l=(navigator.language||"").toLowerCase();'
            f'if(/{BOT_RE}/i.test(navigator.userAgent)||localStorage.getItem("ls_lang"))return;'
            f'if({cond})location.replace("{other_path}")}}catch(e){{}}}})()</script>')


def head(lang, title, desc, path, alt_path, ld, og_type='website'):
    canon = SITE + url(lang, path)
    ko_url, en_url = (SITE + path, SITE + '/en' + path)
    other = url('en' if lang == 'ko' else 'ko', path) if alt_path else None
    return f'''<!doctype html>
<html lang="{lang}">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="theme-color" content="#07080b" />
    {lang_script(lang, other) if other else '<script>document.documentElement.classList.add("js")</script>'}
    <title>{title}</title>
    <meta name="description" content="{desc}" />
    <meta name="robots" content="index, follow" />
    <link rel="canonical" href="{canon}" />
    <link rel="alternate" hreflang="ko" href="{ko_url}" />
    <link rel="alternate" hreflang="en" href="{en_url}" />
    <link rel="alternate" hreflang="x-default" href="{ko_url}" />
    <meta property="og:type" content="{og_type}" />
    <meta property="og:site_name" content="live sub" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{desc}" />
    <meta property="og:url" content="{canon}" />
    <meta property="og:locale" content="{'ko_KR' if lang == 'ko' else 'en_US'}" />
    <meta name="twitter:card" content="summary_large_image" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css" />
    <link rel="stylesheet" href="/home.css?v={CSS_V}" />
    <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
  </head>
  <body>
    <div class="aurora" aria-hidden="true"></div>
'''


def chrome_top(lang, path):
    d = L[lang]
    other = url('en' if lang == 'ko' else 'ko', path)
    ann = f'<span>{d["ann"]} — <a href="mailto:support@transtream.app">support@transtream.app</a></span><span>✳</span>'
    home = url(lang, '/')
    return f'''    <div class="announce"><div class="wrap"><b><i class="dot"></i><span>{d["annb"]}</span></b><div class="rail"><div class="track">{ann * 6}</div></div></div></div>
    <header class="header"><div class="wrap"><nav class="nav" aria-label="main">
      <a class="logo" href="{home}"><i><b></b><b></b><b></b></i><em class="wm">live<span>sub</span></em></a>
      <div class="links"><a href="{home}#transtream">{d['nav'][0]}</a><a href="{home}#family">{d['nav'][1]}</a><a href="{url(lang, '/guides/')}">{d['nav'][2]}</a></div>
      <div style="display:flex;align-items:center;gap:4px"><a class="lang" href="{other}" data-lang="{d['other']}">{d['otherlabel']}</a><a class="btn btn-lime" href="https://transtream.app" target="_blank" rel="noopener">{d['open']} ↗</a></div>
    </nav></div></header>
'''


def chrome_bottom(lang, path):
    d = L[lang]
    other = url('en' if lang == 'ko' else 'ko', path)
    flinks = ''.join(f'<li><a href="{url(lang, s[3])}">{sname(s, lang)}</a></li>' for s in SITES)
    return f'''    <footer><div class="wrap">
      <div class="fgrid"><div><a class="logo" href="{url(lang, '/')}"><i><b></b><b></b><b></b></i><em class="wm">live<span>sub</span></em></a><p style="max-width:340px;margin-top:14px">{d['fdesc']}</p></div>
        <div><h4>{d['fh'][0]}</h4><ul>{flinks}</ul></div>
        <div><h4>{d['fh'][1]}</h4><ul><li><a href="{url(lang, '/guides/')}">{d['nav'][2]}</a></li><li><a href="{other}" data-lang="{d['other']}">{d['otherfull']}</a></li><li><a href="mailto:support@transtream.app">{d['contact']}</a></li></ul></div></div>
      <div class="fbot"><span>© 2026 live sub. Stay connected.</span><span class="mono">live-sub.com</span></div>
    </div></footer>
    <script>(function(){{document.querySelectorAll('[data-lang]').forEach(function(a){{a.addEventListener('click',function(){{try{{localStorage.setItem('ls_lang',a.dataset.lang)}}catch(e){{}}}})}});var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{threshold:.12}});document.querySelectorAll('.rv').forEach(function(el){{io.observe(el)}})}})()</script>
'''


def write(path, html):
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(html)


def out_path(lang, path):
    p = (L[lang]['prefix'] + path).lstrip('/')
    return os.path.join(p, 'index.html')


def gname(g, lang):
    return g[2] if lang == 'ko' else g[3]


def org_ld(lang):
    return {"@type": "Organization", "@id": SITE + "/#org", "name": "live sub", "alternateName": ["라이브서브", "livesub"], "url": SITE + "/", "email": "support@transtream.app",
            "sameAs": [s[3] for s in SITES if s[3].startswith('http')] + [PLAY]}


# ---------------------------------------------------------------- pages
def home(lang):
    d = L[lang]
    tiles = ''
    for s in SITES:
        href = url(lang, s[3])
        if s[0] == 'trans':
            chips = ''.join(f'<span>{c}</span>' for c in d['trans_chips'])
            tiles += f'<a class="tile t-trans rv" href="{href}"{ext(href)}><span class="tag">01 · LIVE &amp; LANGUAGE</span><span class="go">→</span><h3>Transtream<small>.app</small></h3><p>{d["trans_desc"]}</p><div class="mini-cap"><div><b>EN</b>Welcome back to the stream!</div><div><b>KO</b>다시 방송에 오신 걸 환영해요!</div></div><div class="chips">{chips}</div></a>'
            continue
        i = [x[0] for x in SITES].index(s[0]) + 1
        tag = {'health': 'HEALTH', 'hongbo': 'PROMOTION', 'ssrrr': 'COMMUNITY', 'matda': 'MATCHING', 'tool': 'TOOLS', 'hire': 'HIRING'}[s[0]]
        desc = s[4] if lang == 'ko' else s[5]
        chips = ''.join(f'<span>{c}</span>' for c in (s[7] if lang == 'ko' else s[8]))
        tiles += f'<a class="tile t-{s[0]} rv" href="{href}"{ext(href)}><span class="tag">0{i} · {tag}</span><span class="go">→</span><h3>{sname(s, lang)}<small>{s[6]}</small></h3><p>{desc}</p><div class="chips">{chips}</div></a>'
    steps = ''.join(f'<article class="step rv"><span class="n">0{i + 1}</span><span class="glyph">{g}</span><h3>{h}</h3><p>{p}</p></article>' for i, (g, h, p) in enumerate(d['steps']))
    langchips = ''.join(f'<span{" class=on" if i == 0 else ""}>{c[0]}</span>' for i, c in enumerate(d['caps']))
    wave = ''.join(f'<i style="animation-delay:{(i * 0.09) % 1.1:.2f}s"></i>' for i in range(14))
    plist = ''.join(f'<a href="{url(lang, "/guides/" + g[0] + "-live-translation/")}">{gname(g, lang)}</a>' for g in GUIDES[:7])
    glist = ''.join(f'<a href="{url(lang, "/guides/" + g[0] + "-live-translation/")}">{gname(g, lang)}<span>→</span></a>' for g in GUIDES[:9])
    caps = json.dumps([c[1] for c in d['caps']], ensure_ascii=False)
    items = [{"@type": "ListItem", "position": i + 1, "item": {"@type": "MobileApplication" if s[0] == 'health' else "WebSite", "name": sname(s, lang), "alternateName": ALT.get(sname(s, lang), ''), "url": (SITE + url(lang, s[3])) if s[3].startswith('/') else s[3], "description": s[4] if lang == 'ko' else s[5]}} for i, s in enumerate(SITES)]
    ld = {"@context": "https://schema.org", "@graph": [org_ld(lang), {"@type": "WebSite", "@id": SITE + "/#website", "name": "live sub", "url": SITE + "/", "inLanguage": lang, "publisher": {"@id": SITE + "/#org"}}, {"@type": "ItemList", "name": "live sub family sites", "itemListElement": items}]}
    html = head(lang, d['home_title'], d['home_desc'], '/', True, ld) + chrome_top(lang, '/') + f'''    <main>
      <section class="hero" id="transtream"><div class="gridbg"></div><div class="wrap">
        <span class="pill rv"><em>LIVE</em>{d['pill']}</span>
        <h1 class="rv">{d['h1']}</h1>
        <p class="lede rv">{d['lede']}</p>
        <div class="cta rv"><a class="btn btn-lime" href="https://transtream.app" target="_blank" rel="noopener">{d['start']} ↗</a><a class="btn btn-ghost" href="#family">{d['cta2']} ↓</a></div>
        <div class="demo rv" aria-hidden="true">
          <div class="screen"><div class="bar"><span class="live">● LIVE</span><span class="viewers mono">{d['viewers']}</span></div>
            <div class="chip-lang">{langchips}</div>
            <div class="wave">{wave}</div>
            <div class="caption"><div class="src">{d['src']}</div><div class="out" id="capout">{d['caps'][0][1]}</div></div></div>
          <div class="float f1"><span class="ic">✦</span><span><small>{d['f1'][0]}</small><strong>{d['f1'][1]}</strong></span></div>
          <div class="float f2"><span class="ic">◉</span><span><small>{d['f2'][0]}</small><strong>{d['f2'][1]}</strong></span></div>
        </div>
      </div></section>
      <section class="platforms"><div class="wrap"><p>{d['plat']}</p><div class="plist">{plist}</div></div></section>
      <section class="sec" id="how"><div class="wrap">
        <div class="head-row rv"><div><div class="eyebrow">{d['howE']}</div><h2>{d['howH']}</h2></div><p class="sub">{d['howS']}</p></div>
        <div class="steps">{steps}</div>
      </div></section>
      <section class="sec" id="family"><div class="wrap">
        <div class="head-row rv"><div><div class="eyebrow">{d['famE']}</div><h2>{d['famH']}</h2></div><p class="sub">{d['famS']}</p></div>
        <div class="bento">{tiles}</div>
      </div></section>
      <section class="sec" id="guides"><div class="wrap">
        <div class="head-row rv"><div><div class="eyebrow">{d['gE']}</div><h2>{d['gH']}</h2></div><a class="btn btn-ghost" href="{url(lang, '/guides/')}">{d['gAll']} →</a></div>
        <div class="glist rv">{glist}</div>
      </div></section>
      <div class="wrap"><section class="final rv"><h2>{d['fin']}</h2><p>{d['finS']}</p><a class="btn btn-lime" href="https://transtream.app" target="_blank" rel="noopener">{d['start']} ↗</a></section></div>
    </main>
''' + chrome_bottom(lang, '/') + f'''    <script>(function(){{var caps={caps},i=0,out=document.getElementById('capout'),chips=document.querySelectorAll('.chip-lang span');setInterval(function(){{i=(i+1)%caps.length;out.style.opacity=0;setTimeout(function(){{out.textContent=caps[i];out.style.opacity=1;chips.forEach(function(c,j){{c.classList.toggle('on',j===i)}})}},300)}},3200)}})()</script>
  </body>
</html>
'''
    write(out_path(lang, '/'), html)


def guides_index(lang):
    d = L[lang]
    def cards(kind):
        return ''.join(f'<a class="gcard rv" href="{url(lang, "/guides/" + g[0] + "-live-translation/")}"><small>{"LIVE STREAM" if kind == "stream" else "MEETING · CALL"}</small><h3>{gname(g, lang)}</h3><p>{(g[5] if lang == "ko" else g[6])}</p><span class="go">→</span></a>' for g in GUIDES if g[1] == kind)
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": d['g_title'], "url": SITE + url(lang, '/guides/'), "inLanguage": lang, "publisher": org_ld(lang)}
    html = head(lang, d['g_title'], d['g_desc'], '/guides/', True, ld) + chrome_top(lang, '/guides/') + f'''    <main>
      <section class="hero hero-sm"><div class="gridbg"></div><div class="wrap">
        <span class="pill rv"><em>GUIDES</em>{d['gE']}</span>
        <h1 class="rv">{d['g_h1']}</h1>
        <p class="lede rv">{d['g_lede']}</p>
      </div></section>
      <section class="sec sec-tight"><div class="wrap"><div class="eyebrow rv">{d['g_streams']}</div><div class="gcards">{cards('stream')}</div></div></section>
      <section class="sec sec-tight"><div class="wrap"><div class="eyebrow rv">{d['g_meetings']}</div><div class="gcards">{cards('meeting')}</div><p class="note">{d['g_note']}</p></div></section>
    </main>
''' + chrome_bottom(lang, '/guides/') + '  </body>\n</html>\n'
    write(out_path(lang, '/guides/'), html)


def guide_page(lang, g):
    d = L[lang]
    path = f"/guides/{g[0]}-live-translation/"
    name = gname(g, lang)
    intro = g[5] if lang == 'ko' else g[6]
    tips = g[7] if lang == 'ko' else g[8]
    faqs = d['faqs'](g)
    li = lambda xs: ''.join(f'<li>{x}</li>' for x in xs)
    related = [x for x in GUIDES if x[0] != g[0] and x[1] == g[1] and x[0] not in ('stripchat', 'chaturbate')][:4]
    rel = ''.join(f'<a href="{url(lang, "/guides/" + x[0] + "-live-translation/")}">{gname(x, lang)}<span>→</span></a>' for x in related)
    faq_html = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faqs)
    title = d['gp_title'](g)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "HowTo", "name": d['gp_h1'](g), "description": intro, "inLanguage": lang,
         "step": [{"@type": "HowToStep", "position": i + 1, "text": s} for i, s in enumerate(d['steps_g'](g))]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "live sub", "item": SITE + url(lang, '/')},
            {"@type": "ListItem", "position": 2, "name": d['nav'][2], "item": SITE + url(lang, '/guides/')},
            {"@type": "ListItem", "position": 3, "name": name, "item": SITE + url(lang, path)}]}]}
    tips_html = f'<h2>{d["tips"]}</h2><ul>{li(tips)}</ul>' if tips else ''
    html = head(lang, title, d['gp_desc'](g), path, True, ld, 'article') + chrome_top(lang, path) + f'''    <main class="article wrap">
      <a class="back" href="{url(lang, '/guides/')}">{d['back']}</a>
      <div class="eyebrow">{g[4] if lang == 'ko' else 'REAL-TIME TRANSLATION GUIDE'}</div>
      <h1>{d['gp_h1'](g)}</h1>
      <p class="lead">{intro}</p>
      <a class="btn btn-lime" href="https://transtream.app" target="_blank" rel="noopener">{d['start']} ↗</a>
      <h2>{d['need']}</h2><ul>{li(d['needs'](g))}</ul>
      <h2>{d['setup']}</h2><ol class="steps-ol">{li(d['steps_g'](g))}</ol>
      {tips_html}
      <h2>{d['trouble']}</h2><p>{d['trouble_t']}</p>
      <h2>{d['faq']}</h2><div class="faq">{faq_html}</div>
      <p class="note">{d['notice'](g)}</p>
      {f'<h2>{d["related"]}</h2><div class="glist">{rel}</div>' if rel else ''}
    </main>
''' + chrome_bottom(lang, path) + '  </body>\n</html>\n'
    write(out_path(lang, path), html)


def healthy(lang):
    d = L[lang]
    path = '/healthyroutine/'
    feats = ''.join(f'<article class="step rv"><span class="n">0{i + 1} / {k}</span><h3>{h}</h3><p>{p}</p></article>' for i, (k, h, p) in enumerate(d['hr_f']))
    ld = {"@context": "https://schema.org", "@type": "MobileApplication", "name": d['hr_name'], "alternateName": ALT[d['hr_name']], "operatingSystem": "Android",
          "applicationCategory": "HealthApplication", "url": SITE + url(lang, path), "installUrl": PLAY, "inLanguage": lang,
          "offers": {"@type": "Offer", "price": "0", "priceCurrency": "KRW"}, "description": d['hr_desc'], "publisher": org_ld(lang)}
    html = head(lang, d['hr_title'], d['hr_desc'], path, True, ld) + chrome_top(lang, path) + f'''    <main>
      <section class="hero hero-sm"><div class="gridbg"></div><div class="wrap">
        <span class="pill rv"><em>APP</em>{d['hr_name']}</span>
        <h1 class="rv">{d['hr_h1']}</h1>
        <p class="lede rv">{d['hr_lede']}</p>
        <div class="cta rv"><a class="btn btn-lime" href="{PLAY}" target="_blank" rel="noopener">{d['hr_dl']} ↗</a><a class="btn btn-ghost" href="{url(lang, '/#family')}">{d['cta2']}</a></div>
      </div></section>
      <section class="sec sec-tight"><div class="wrap"><div class="steps">{feats}</div><p class="note">{d['hr_note']}</p></div></section>
    </main>
''' + chrome_bottom(lang, path) + '  </body>\n</html>\n'
    write(out_path(lang, path), html)


def sitemap():
    paths = ['/', '/guides/', '/healthyroutine/'] + [f"/guides/{g[0]}-live-translation/" for g in GUIDES]
    rows = ''
    for p in paths:
        for lang in ('ko', 'en'):
            rows += f'  <url><loc>{SITE}{url(lang, p)}</loc><lastmod>{TODAY}</lastmod></url>\n'
    write('sitemap.xml', f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{rows}</urlset>\n')


for lang in ('ko', 'en'):
    home(lang)
    guides_index(lang)
    healthy(lang)
    for g in GUIDES:
        guide_page(lang, g)
sitemap()
print('built', 2 * (3 + len(GUIDES)), 'pages')
