(function () {
  const supported = ['ko', 'en', 'ja', 'es'];
  const browser = (navigator.language || 'en').toLowerCase().split('-')[0];
  const forced = new URLSearchParams(location.search).get('lang')?.toLowerCase();
  const lang = supported.includes(forced) ? forced : (supported.includes(browser) ? browser : 'en');
  const guide = document.querySelector('[data-guide]')?.dataset.guide;
  const names = { chaturbate: 'Chaturbate', stripchat: 'Stripchat', soop: 'SOOP', chzzk: 'CHZZK', youtube: 'YouTube Live', tiktok: 'TikTok LIVE', twitch: 'Twitch' };
  const copy = {
    en: { kicker:'REAL-TIME LIVE STREAM TRANSLATION', back:'← Platform guides', title:p=>`How to Translate ${names[p]} Streams`, lead:p=>`Transtream translates ${names[p]} browser audio into real-time subtitles for multilingual viewing.`, notice:p=>`${names[p]} is a trademark of its respective owner. Transtream and live sub are independent services and are not affiliated with or endorsed by ${names[p]}.`, need:'What you need', setup:'Setup steps', trouble:'If captions do not appear', limits:'Important limitations', items:['A desktop browser with the live stream open in a tab','Transtream open in another tab or window','Your preferred subtitle language'], steps:p=>[`Open the ${names[p]} live stream in a desktop browser.`,`Open Transtream and start a translation session.`,`Select the browser tab or system audio source containing the stream.`,`Choose the spoken language and subtitle language.`,`Keep the stream audio enabled and adjust the subtitle panel position.`], troubleText:'Check the selected audio source, browser permissions, mute state, and language setting. Reconnect the source after reopening the stream tab.', limitsText:'Transtream processes only browser audio made available to the session. It does not host, record, download, or redistribute the live stream.' },
    ko: { kicker:'실시간 라이브 스트림 번역', back:'← 플랫폼 가이드', title:p=>`${names[p]} 라이브 방송 번역 방법`, lead:p=>`Transtream은 ${names[p]}의 브라우저 오디오를 실시간 자막으로 변환해 여러 언어로 시청할 수 있도록 합니다.`, notice:p=>`${names[p]}은(는) 해당 소유자의 상표입니다. Transtream과 live sub는 ${names[p]}와 제휴하거나 승인받은 서비스가 아닙니다.`, need:'준비물', setup:'설정 방법', trouble:'자막이 나타나지 않을 때', limits:'중요한 제한사항', items:['라이브 방송이 열린 데스크톱 브라우저','다른 탭이나 창에서 연 Transtream','사용할 자막 언어'], steps:p=>[`${names[p]} 라이브 방송을 데스크톱 브라우저에서 엽니다.`,'Transtream을 열고 번역 세션을 시작합니다.','방송이 재생되는 브라우저 탭 또는 시스템 오디오를 선택합니다.','음성 언어와 자막 언어를 선택합니다.','방송 오디오를 켜고 자막 패널 위치를 조정합니다.'], troubleText:'선택한 오디오 소스, 브라우저 권한, 음소거 상태, 언어 설정을 확인하세요. 방송 탭을 다시 연 뒤 소스를 다시 연결해 보세요.', limitsText:'Transtream은 세션에 제공된 브라우저 오디오만 처리합니다. 라이브 방송을 호스팅하거나 녹화·다운로드·재배포하지 않습니다.' },
    ja: { kicker:'リアルタイムライブ配信翻訳', back:'← プラットフォームガイド', title:p=>`${names[p]}ライブ配信を翻訳する方法`, lead:p=>`Transtreamは${names[p]}のブラウザ音声をリアルタイム字幕に変換し、多言語で視聴できるようにします。`, notice:p=>`${names[p]}は各所有者の商標です。Transtreamとlive subは${names[p]}と提携・承認されたサービスではありません。`, need:'必要なもの', setup:'設定手順', trouble:'字幕が表示されない場合', limits:'重要な制限', items:['ライブ配信を開いたデスクトップブラウザ','別のタブまたはウィンドウで開いたTranstream','希望する字幕言語'], steps:p=>[`${names[p]}のライブ配信をデスクトップブラウザで開きます。`,'Transtreamを開き、翻訳セッションを開始します。','配信音声のあるブラウザタブまたはシステム音声を選択します。','音声言語と字幕言語を選択します。','配信音声を有効にし、字幕パネルの位置を調整します。'], troubleText:'音声ソース、ブラウザ権限、ミュート状態、言語設定を確認してください。配信タブを開き直した場合はソースを再接続します。', limitsText:'Transtreamはセッションに提供されたブラウザ音声のみを処理します。配信のホスティング、録画、ダウンロード、再配布は行いません。' },
    es: { kicker:'TRADUCCIÓN DE DIRECTOS EN TIEMPO REAL', back:'← Guías de plataformas', title:p=>`Cómo traducir directos de ${names[p]}`, lead:p=>`Transtream convierte el audio del navegador de ${names[p]} en subtítulos en tiempo real para ver directos en varios idiomas.`, notice:p=>`${names[p]} es una marca de su respectivo propietario. Transtream y live sub son servicios independientes y no están afiliados ni respaldados por ${names[p]}.`, need:'Qué necesitas', setup:'Pasos de configuración', trouble:'Si no aparecen los subtítulos', limits:'Limitaciones importantes', items:['Un navegador de escritorio con el directo abierto','Transtream abierto en otra pestaña o ventana','El idioma de subtítulos que prefieras'], steps:p=>[`Abre el directo de ${names[p]} en un navegador de escritorio.`,'Abre Transtream e inicia una sesión de traducción.','Selecciona la pestaña del navegador o el audio del sistema donde se reproduce el directo.','Elige el idioma hablado y el idioma de los subtítulos.','Mantén activo el audio y ajusta la posición del panel de subtítulos.'], troubleText:'Comprueba la fuente de audio, los permisos del navegador, el estado de silencio y el idioma seleccionado. Vuelve a conectar la fuente después de abrir de nuevo la pestaña.', limitsText:'Transtream solo procesa el audio del navegador disponible para la sesión. No aloja, graba, descarga ni redistribuye el directo.' }
  }[lang];
  if (!guide || !copy) return;
  document.documentElement.lang = lang;
  document.title = `${copy.title(guide)} | live sub`;
  const q = s => document.querySelector(s);
  q('.back').textContent = copy.back;
  q('.kicker').textContent = `/ ${copy.kicker}`;
  q('.article h1').textContent = copy.title(guide);
  q('.lead').textContent = copy.lead(guide);
  q('.notice').textContent = copy.notice(guide);
  const headings = q('.article').querySelectorAll('h2');
  headings[0].textContent = copy.need; headings[1].textContent = copy.setup; headings[2].textContent = copy.trouble; headings[3].textContent = copy.limits;
  q('.article ul').innerHTML = copy.items.map(item => `<li>${item}</li>`).join('');
  q('.article ol').innerHTML = copy.steps(guide).map(item => `<li>${item}</li>`).join('');
  const paragraphs = q('.article').querySelectorAll('p');
  paragraphs[paragraphs.length - 2].textContent = copy.troubleText;
  paragraphs[paragraphs.length - 1].textContent = copy.limitsText;
})();
