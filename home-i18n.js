(function () {
  const lang = ['ko','en','ja','es'].includes((navigator.language || 'en').toLowerCase().split('-')[0]) ? (navigator.language || 'en').toLowerCase().split('-')[0] : 'en';
  const c = {
    en:{section:'/ MORE FROM LIVE SUB',heading:'One curious mind.<br><em>Four useful worlds.</em>',intro:'Beyond live streams, we build useful tools for the next scene of work and everyday life.',cards:[['01 / LIVE & LANGUAGE','transtream','.app','Real-time translation for global live streams and video calls.'],['02 / EVERYDAY TOOLS','manytool','.net','A collection of small, genuinely useful online tools.'],['03 / WORK & PEOPLE','hireroom','.net','A simple hiring page for small and growing teams.'],['04 / HEALTH & ROUTINE','Healthy','Routine','An app for workout records and routine management.']],chips:['FPS sensitivity','LoL champions','Color picks'],hire:'Product designer',app:'Workout tracker',whyLabel:'/ MADE FOR THE MOMENT',whyTitle:'Keep your eyes<br>on <em>what matters.</em>',whyStat:'languages, one<br>shared experience',whyNote:'Technology can be complex.<br>Connection should feel light.'},
    ko:{section:'/ MORE FROM LIVE SUB',heading:'One curious mind.<br><em>Four useful worlds.</em>',intro:'라이브를 넘어, 일과 생활의 다음 장면까지.<br>필요한 순간에 필요한 도구를 만듭니다.',cards:[['01 / LIVE & LANGUAGE','transtream','.app','글로벌 라이브 방송과<br>화상통화를 위한 실시간 번역.'],['02 / EVERYDAY TOOLS','manytool','.net','작지만 확실히 유용한<br>온라인 도구 모음.'],['03 / WORK & PEOPLE','hireroom','.net','중소기업도 쉽게 만드는<br>우리만의 채용 페이지.'],['04 / HEALTH & ROUTINE','헬띠','루틴','운동 기록과<br>루틴 관리를 위한 앱.']],chips:['FPS 감도','롤 챔프','컬러 추천'],hire:'Product designer',app:'Workout tracker',whyLabel:'/ MADE FOR THE MOMENT',whyTitle:'Keep your eyes<br>on <em>what matters.</em>',whyStat:'languages, one<br>shared experience',whyNote:'기술은 복잡해도<br>연결은 가벼워야 하니까.'},
    ja:{section:'/ LIVE SUBのプロダクト',heading:'ひとつの好奇心。<br><em>4つの役立つ世界。</em>',intro:'ライブ配信を越えて、仕事と日常の次の場面に役立つツールを作ります。',cards:[['01 / LIVE & LANGUAGE','transtream','.app','グローバルなライブ配信とビデオ通話のリアルタイム翻訳。'],['02 / EVERYDAY TOOLS','manytool','.net','小さくても確かに役立つオンラインツール集。'],['03 / WORK & PEOPLE','hireroom','.net','中小企業のためのシンプルな採用ページ。'],['04 / HEALTH & ROUTINE','ヘルシー','ルーティン','運動記録とルーティン管理のためのアプリ。']],chips:['FPS感度','LoLチャンピオン','カラー提案'],hire:'Product designer',app:'Workout tracker',whyLabel:'/ MADE FOR THE MOMENT',whyTitle:'大切なものに<br><em>集中しよう。</em>',whyStat:'languages, one<br>shared experience',whyNote:'技術は複雑でも、<br>つながりは軽やかに。'},
    es:{section:'/ MÁS DE LIVE SUB',heading:'Una mente curiosa.<br><em>Cuatro mundos útiles.</em>',intro:'Más allá de los directos, creamos herramientas útiles para el trabajo y la vida diaria.',cards:[['01 / LIVE & LANGUAGE','transtream','.app','Traducción en tiempo real para directos y videollamadas globales.'],['02 / EVERYDAY TOOLS','manytool','.net','Una colección de pequeñas herramientas online realmente útiles.'],['03 / WORK & PEOPLE','hireroom','.net','Una página de contratación sencilla para equipos pequeños.'],['04 / HEALTH & ROUTINE','Healthy','Routine','Una app para registrar entrenamientos y gestionar rutinas.']],chips:['Sensibilidad FPS','Campeones de LoL','Colores'],hire:'Product designer',app:'Workout tracker',whyLabel:'/ HECHO PARA EL MOMENTO',whyTitle:'Mira lo que<br><em>importa.</em>',whyStat:'languages, one<br>shared experience',whyNote:'La tecnología puede ser compleja.<br>La conexión debe sentirse ligera.'}
  }[lang];
  const q = s => document.querySelector(s);
  const qa = s => document.querySelectorAll(s);
  if (!c || !q('.ecosystem')) return;
  document.querySelector('.ecosystem .section-label').textContent = c.section;
  q('.ecosystem-heading h2').innerHTML = c.heading;
  q('.ecosystem-heading p').innerHTML = c.intro;
  qa('.world-card').forEach((card, i) => { const x=c.cards[i]; card.querySelector('.world-tag').textContent=x[0]; card.querySelector('h3').innerHTML=x[1]+'<span>'+x[2]+'</span>'; card.querySelector('p').innerHTML=x[3]; });
  const chips = q('.tool-chips'); if (chips) chips.innerHTML = c.chips.map(x=>`<span>${x}</span>`).join('');
  const hire = q('.hire-line span'); if (hire) hire.textContent = c.hire;
  const app = q('.app-line span'); if (app) app.textContent = c.app;
  q('.why .section-label').textContent = c.whyLabel;
  q('.why h2').innerHTML = c.whyTitle;
  q('.why-stat p').innerHTML = c.whyStat;
  q('.why-note p').innerHTML = c.whyNote;
})();
