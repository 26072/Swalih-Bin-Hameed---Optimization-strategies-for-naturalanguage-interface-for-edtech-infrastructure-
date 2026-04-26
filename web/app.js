// ================================================================
// app.js — EduBot Web UI (Flask Backend Edition)
// Project : Optimization Strategies for Natural Language Interface
//           for EdTech Infrastructure
// Roll No : PRJN26-127
//
// This file is the FRONTEND only — it sends the user's message
// to the Python Flask backend (/chat) via fetch() and displays
// whatever Python's matcher.py returns.
// ================================================================

// ── QUICK COMMANDS ────────────────────────────────────────────────
const QUICK_COMMANDS = [
  { label: "🏠  Show Status",        cmd: "show status" },
  { label: "📋  List Courses",       cmd: "list courses" },
  { label: "📌  Assignment Status",  cmd: "assignment status" },
  { label: "📊  My Grades",          cmd: "grades" },
  { label: "📈  My Progress",        cmd: "progress" },
  { label: "🗓️   Schedule",          cmd: "schedule" },
  { label: "👩‍🏫  Faculty",           cmd: "faculty" },
  { label: "💰  Course Fees",        cmd: "course fee" },
  { label: "📚  Resources",          cmd: "resources" },
  { label: "📞  Contact Support",    cmd: "contact" },
];

// ── DOM REFS ──────────────────────────────────────────────────────
const chatWindow      = document.getElementById('chatWindow');
const userInput       = document.getElementById('userInput');
const sendBtn         = document.getElementById('sendBtn');
const typingIndicator = document.getElementById('typingIndicator');
const clearBtn        = document.getElementById('clearBtn');
const menuBtn         = document.getElementById('menuBtn');
const sidebar         = document.getElementById('sidebar');
const sidebarClose    = document.getElementById('sidebarClose');
const quickBtns       = document.getElementById('quickBtns');

// ── INIT ──────────────────────────────────────────────────────────
function init() {
  // Build quick buttons in sidebar
  QUICK_COMMANDS.forEach(({ label, cmd }) => {
    const btn = document.createElement('button');
    btn.className = 'quick-btn';
    btn.textContent = label;
    btn.addEventListener('click', () => sendMessage(cmd));
    quickBtns.appendChild(btn);
  });

  // Show welcome card
  showWelcome();

  // Events
  sendBtn.addEventListener('click', handleSend);
  userInput.addEventListener('keydown', e => { if (e.key === 'Enter') handleSend(); });
  clearBtn.addEventListener('click', clearChat);
  menuBtn.addEventListener('click', () => sidebar.classList.toggle('open'));
  sidebarClose.addEventListener('click', () => sidebar.classList.remove('open'));
  document.addEventListener('click', e => {
    if (!sidebar.contains(e.target) && !menuBtn.contains(e.target)) {
      sidebar.classList.remove('open');
    }
  });
}

// ── WELCOME CARD ──────────────────────────────────────────────────
function showWelcome() {
  const card = document.createElement('div');
  card.className = 'welcome-card';
  card.id = 'welcomeCard';
  card.innerHTML = `
    <h1>Welcome to <span>EduBot</span> 🎓</h1>
    <p>Your AI-powered EdTech assistant — powered by a <strong>Python Flask backend</strong>.<br/>
    Ask me anything about courses, assignments, grades, schedules and more!</p>
    <div class="welcome-chips">
      <span class="chip" data-cmd="help">📚 Help</span>
      <span class="chip" data-cmd="show status">✅ Status</span>
      <span class="chip" data-cmd="list courses">📋 Courses</span>
      <span class="chip" data-cmd="grades">📊 Grades</span>
      <span class="chip" data-cmd="schedule">🗓️ Schedule</span>
      <span class="chip" data-cmd="contact">📞 Contact</span>
    </div>
    <p style="margin-top:16px; font-size:11px; color:#6c63ff;">
      🐍 Powered by Python · Flask · Basic String Matching
    </p>
  `;
  card.querySelectorAll('.chip').forEach(chip => {
    chip.addEventListener('click', () => sendMessage(chip.dataset.cmd));
  });
  chatWindow.appendChild(card);
}

// ── MESSAGE HANDLING ──────────────────────────────────────────────
function handleSend() {
  const text = userInput.value.trim();
  if (!text) return;
  sendMessage(text);
  userInput.value = '';
  userInput.focus();
}

async function sendMessage(text) {
  // Remove welcome card on first message
  const wc = document.getElementById('welcomeCard');
  if (wc) wc.remove();

  // Show user bubble
  appendMessage('user', text);

  // Close sidebar on mobile
  sidebar.classList.remove('open');

  // Disable input while waiting
  userInput.disabled = true;
  sendBtn.disabled   = true;

  // Show typing indicator
  typingIndicator.classList.add('show');
  scrollToBottom();

  try {
    // ── CALL PYTHON FLASK BACKEND ─────────────────────────────────
    // POST to /chat with the user's message as JSON
    // Python's matcher.py does the real matching work
    const res = await fetch('/chat', {
      method : 'POST',
      headers: { 'Content-Type': 'application/json' },
      body   : JSON.stringify({ message: text })
    });

    const data = await res.json();

    // Hide typing indicator
    typingIndicator.classList.remove('show');

    // Show bot response
    appendMessage('bot', data.response || 'Sorry, something went wrong.');

    // Handle farewell — disable input if user said bye
    if (data.farewell) {
      setTimeout(() => {
        userInput.disabled   = true;
        sendBtn.disabled     = true;
        userInput.placeholder = 'Session ended. Refresh to start again.';
      }, 800);
      return; // don't re-enable input
    }

  } catch (err) {
    // ── ERROR: Flask server not running ──────────────────────────
    typingIndicator.classList.remove('show');
    appendMessage('bot',
      '⚠️  Cannot connect to Python backend.\n\n' +
      'Make sure the Flask server is running:\n' +
      '  1. Open your terminal\n' +
      '  2. cd into the edtech_chatbot folder\n' +
      '  3. Run: python web_server.py\n' +
      '  4. Then refresh this page at http://localhost:5000'
    );
  }

  // Re-enable input
  userInput.disabled = false;
  sendBtn.disabled   = false;
}

// ── APPEND MESSAGE BUBBLE ────────────────────────────────────────
function appendMessage(role, text) {
  const row = document.createElement('div');
  row.className = `msg-row ${role}`;

  const avatar = document.createElement('div');
  avatar.className = 'msg-avatar';
  avatar.textContent = role === 'bot' ? '🤖' : '🎓';

  const bubble = document.createElement('div');
  bubble.className = 'msg-bubble';
  bubble.textContent = text;

  const time = document.createElement('div');
  time.className = 'msg-time';
  time.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

  const wrap = document.createElement('div');
  wrap.style.cssText = `display:flex; flex-direction:column; max-width:72%;`;
  if (role === 'user') wrap.style.alignItems = 'flex-end';

  wrap.appendChild(bubble);
  wrap.appendChild(time);

  if (role === 'bot') {
    row.appendChild(avatar);
    row.appendChild(wrap);
  } else {
    row.appendChild(wrap);
    row.appendChild(avatar);
  }

  chatWindow.appendChild(row);
  scrollToBottom();
}

function scrollToBottom() {
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function clearChat() {
  chatWindow.innerHTML = '';
  userInput.disabled   = false;
  sendBtn.disabled     = false;
  userInput.placeholder = "Type a message… e.g. 'show status', 'list courses', 'help'";
  showWelcome();
}

// ── START ─────────────────────────────────────────────────────────
init();
