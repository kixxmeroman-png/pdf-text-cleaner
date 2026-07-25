import os
from weasyprint import HTML

# Create standard HTML file for standard single-page / multi-page web app solution guide or code template, but wait, the user wants a full working code file or ready-to-use HTML/JS file that they can upload to GitHub Pages!
# Wait, the prompt is asking for full code ("나는 코딩을 할 줄 몰라서 네가 처음부터 다 짜줘야할 거야. 도와줘.").
# Can we build a single `index.html` file that contains everything (HTML, CSS, JS with pdf.js, clean logic, UI, copy & txt download, and spelling check integration) and also provide a single clickable download or generate an HTML/JS file for them to deploy or download?
# Let's generate a complete single-file `index.html` (which can be hosted directly on GitHub Pages or run locally in a browser!) AND generate a downloadable ZIP or HTML file for them, along with clear step-by-step instructions on how to put it on GitHub Pages.

html_content = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PDF & 텍스트 줄바꿈 정돈 및 맞춤법 검사기</title>
  <!-- PDF.js CDN -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
  <style>
    :root {
      --primary-color: #4a6fa5;
      --primary-hover: #3b5984;
      --bg-color: #f8f9fa;
      --card-bg: #ffffff;
      --border-color: #e9ecef;
      --text-main: #333333;
      --text-sub: #6c757d;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      background-color: var(--bg-color);
      color: var(--text-main);
      line-height: 1.6;
      padding: 20px;
    }

    .container {
      max-width: 1000px;
      margin: 0 auto;
      background-color: var(--card-bg);
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
      padding: 30px;
    }

    header {
      text-align: center;
      margin-bottom: 25px;
      padding-bottom: 15px;
      border-bottom: 2px solid var(--border-color);
    }

    header h1 {
      font-size: 1.8rem;
      color: var(--primary-color);
      margin-bottom: 8px;
    }

    header p {
      color: var(--text-sub);
      font-size: 0.95rem;
    }

    .upload-section {
      background-color: #f1f5f9;
      border: 2px dashed #cbd5e1;
      border-radius: 8px;
      padding: 20px;
      text-align: center;
      margin-bottom: 20px;
      transition: all 0.2s ease;
    }

    .upload-section:hover {
      border-color: var(--primary-color);
      background-color: #eef2ff;
    }

    .file-input-btn {
      display: inline-block;
      padding: 10px 20px;
      background-color: var(--primary-color);
      color: white;
      border-radius: 6px;
      cursor: pointer;
      font-weight: 600;
      font-size: 0.95rem;
      transition: background-color 0.2s;
    }

    .file-input-btn:hover {
      background-color: var(--primary-hover);
    }

    input[type="file"] {
      display: none;
    }

    .editor-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 20px;
    }

    @media (max-width: 768px) {
      .editor-grid {
        grid-template-columns: 1fr;
      }
    }

    .editor-box {
      display: flex;
      flex-direction: column;
    }

    .editor-box label {
      font-weight: 600;
      margin-bottom: 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    textarea {
      width: 100%;
      height: 380px;
      padding: 12px;
      border: 1fr solid var(--border-color);
      border-radius: 6px;
      border: 1px solid #ccc;
      font-size: 0.95rem;
      line-height: 1.6;
      resize: vertical;
      outline: none;
      font-family: inherit;
    }

    textarea:focus {
      border-color: var(--primary-color);
      box-shadow: 0 0 0 3px rgba(74, 111, 165, 0.2);
    }

    .btn-group {
      display: flex;
      gap: 10px;
      justify-content: center;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }

    button {
      padding: 12px 24px;
      border: none;
      border-radius: 6px;
      font-size: 0.95rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }

    .btn-primary {
      background-color: var(--primary-color);
      color: white;
    }

    .btn-primary:hover {
      background-color: var(--primary-hover);
    }

    .btn-secondary {
      background-color: #64748b;
      color: white;
    }

    .btn-secondary:hover {
      background-color: #475569;
    }

    .btn-outline {
      background-color: transparent;
      border: 1px solid var(--border-color);
      color: var(--text-main);
    }

    .btn-outline:hover {
      background-color: #f1f5f9;
    }

    .status-msg {
      text-align: center;
      font-size: 0.9rem;
      color: var(--primary-color);
      min-height: 24px;
      margin-bottom: 10px;
      font-weight: 500;
    }

    .info-footer {
      font-size: 0.85rem;
      color: var(--text-sub);
      background-color: #f8fafc;
      padding: 15px;
      border-radius: 6px;
      border-left: 4px solid var(--primary-color);
    }
  </style>
</head>
<body>

<div class="container">
  <header>
    <h1>📄 PDF & 텍스트 줄바꿈 정돈기</h1>
    <p>PDF를 올리거나 텍스트를 붙여넣으면 깨진 줄바꿈을 문맥에 맞게 깔끔하게 연결해 드립니다.</p>
  </header>

  <div class="upload-section">
    <label for="pdf-upload" class="file-input-btn">📁 PDF 파일 불러오기</label>
    <input type="file" id="pdf-upload" accept="application/pdf">
    <span id="file-name" style="margin-left: 10px; color: var(--text-sub); font-size: 0.9rem;">선택된 파일 없음</span>
  </div>

  <div class="editor-grid">
    <div class="editor-box">
      <label for="input-text">원본 텍스트 (PDF 내용 또는 직접 입력)</label>
      <textarea id="input-text" placeholder="여기에 텍스트를 직접 붙여넣거나 위에서 PDF 파일을 선택하세요..."></textarea>
    </div>
    <div class="editor-box">
      <label for="output-text">정돈된 텍스트</label>
      <textarea id="output-text" placeholder="줄바꿈 정돈 결과가 여기에 표시됩니다..." readonly></textarea>
    </div>
  </div>

  <div class="status-msg" id="status-msg"></div>

  <div class="btn-group">
    <button class="btn-primary" onclick="processText()">✨ 줄바꿈 정돈하기</button>
    <button class="btn-secondary" onclick="checkSpelling()">🔍 맞춤법 검사 (부산대 검사기 연결)</button>
    <button class="btn-outline" onclick="copyResult()">📋 결과 복사</button>
    <button class="btn-outline" onclick="downloadTxt()">💾 txt 파일로 저장</button>
  </div>

  <div class="info-footer">
    💡 <strong>안내:</strong><br>
    - <code>합\n니다</code>처럼 단어 중간에서 끊긴 줄바꿈은 하나로 합치고, <code>합니다.\n그래서</code>처럼 문장이 끝난 줄바꿈은 띄어쓰기로 변경합니다.<br>
    - 부산대학교 맞춤법 검사기는 보안 정책(CORS)으로 인해 새 창에서 정돈된 텍스트와 함께 연결됩니다.
  </div>
</div>

<script>
  // pdf.js worker 설정
  pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';

  const fileInput = document.getElementById('pdf-upload');
  const fileNameSpan = document.getElementById('file-name');
  const inputText = document.getElementById('input-text');
  const outputText = document.getElementById('output-text');
  const statusMsg = document.getElementById('status-msg');

  // PDF 파일 읽기
  fileInput.addEventListener('change', async function(e) {
    const file = e.target.files[0];
    if (!file) return;

    fileNameSpan.textContent = file.name;
    statusMsg.textContent = 'PDF 텍스트 추출 중...';

    try {
      const arrayBuffer = await file.arrayBuffer();
      const pdf = await pdfjsLib.getDocument({ data: arrayBuffer }).promise;
      let fullText = '';

      for (let i = 1; i <= pdf.numPages; i++) {
        const page = await pdf.getPage(i);
        const textContent = await page.getTextContent();
        const pageText = textContent.items.map(item => item.str).join(' ');
        fullText += pageText + '\n\n';
      }

      inputText.value = fullText.trim();
      statusMsg.textContent = '✅ PDF 텍스트 추출 완료!';
      processText(); // 추출 완료 후 자동 정돈 실행
    } catch (err) {
      console.error(err);
      statusMsg.textContent = '❌ PDF를 읽는 도중 오류가 발생했습니다.';
    }
  });

  // 줄바꿈 정돈 지능형 알고리즘
  function cleanLineBreaks(text) {
    if (!text) return '';

    // 1. 연속된 줄바꿈(2개 이상)은 문단 나누기로 간주하여 임시 토큰으로 보호
    let processed = text.replace(/\n\s*\n/g, '___PARAGRAPH___');

    // 2. 단어 중간에 어색하게 잘린 한국어 줄바꿈 (예: 합\n니다 -> 합니다)
    // 앞글자가 한글이고, 뒷글자가 한글일 때 문장 부호(. ! ?)가 없으면 연결
    processed = processed.replace(/([가-힣a-zA-Z0-9,])\n([가-힣a-zA-Z0-9])/g, function(match, p1, p2) {
      // 숫자 간의 줄바꿈 또는 쉼표 뒤 등 세부 패턴 처리
      return p1 + p2;
    });

    // 3. 문장 종결 부호(. ! ?) 뒤의 줄바꿈은 띄어쓰기로 변경 (예: 합니다.\n그래서 -> 합니다. 그래서)
    processed = processed.replace(/([.!?])\n([가-힣a-zA-Z0-9])/g, '$1 $2');

    // 4. 일반 남은 단일 줄바꿈은 띄어쓰기로 교체
    processed = processed.replace(/\n/g, ' ');

    // 5. 연속된 공백 제거
    processed = processed.replace(/ +/g, ' ');

    // 6. 임시 토큰으로 보호한 문단 나누기 복원
    processed = processed.replace(/___PARAGRAPH___/g, '\n\n');

    return processed.trim();
  }

  // 버튼 클릭 시 정돈 처리
  function processText() {
    const raw = inputText.value;
    if (!raw) {
      statusMsg.textContent = '텍스트를 입력하거나 PDF 파일을 불러와 주세요.';
      return;
    }
    const result = cleanLineBreaks(raw);
    outputText.value = result;
    statusMsg.textContent = '✨ 줄바꿈 정돈이 완료되었습니다!';
  }

  // 부산대 맞춤법 검사기 연결
  function checkSpelling() {
    const text = outputText.value || inputText.value;
    if (!text) {
      alert('검사할 텍스트가 없습니다.');
      return;
    }

    // 텍스트를 클립보드에 자동 복사 후 부산대 검사기 이동
    navigator.clipboard.writeText(text).then(() => {
      alert('정돈된 텍스트가 클립보드에 복사되었습니다!\n열리는 부산대 맞춤법 검사기 페이지에 붙여넣기(Ctrl+V)하여 검사하세요.');
      window.open('https://speller.cs.pusan.ac.kr/', '_blank');
    }).catch(() => {
      // 클립보드 복사 실패 시 바로 페이지 이동
      window.open('https://speller.cs.pusan.ac.kr/', '_blank');
    });
  }

  // 결과 복사
  function copyResult() {
    if (!outputText.value) {
      alert('복사할 결과가 없습니다.');
      return;
    }
    navigator.clipboard.writeText(outputText.value).then(() => {
      statusMsg.textContent = '📋 정돈된 텍스트가 클립보드에 복사되었습니다!';
    });
  }

  // txt 저장
  function downloadTxt() {
    const text = outputText.value;
    if (!text) {
      alert('저장할 결과가 없습니다.');
      return;
    }
    const blob = new Blob([text], { type: 'text/plain;charset=utf-8' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = '정돈된_텍스트.txt';
    link.click();
    URL.revokeObjectURL(link.href);
    statusMsg.textContent = '💾 txt 파일로 저장되었습니다!';
  }
</script>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Created index.html successfully")