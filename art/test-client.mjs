import fs from 'node:fs';
import vm from 'node:vm';

const code = fs.readFileSync(new URL('../client.js', import.meta.url), 'utf8');

function fakeReact() {
  return {
    createElement(type, props, ...children) {
      return { type, props: props || {}, children };
    },
    useState(initial) {
      return [typeof initial === 'function' ? initial() : initial, () => {}];
    },
    useEffect() {},
  };
}

function run(hour) {
  const captured = { slots: [], tokens: null, locale: null, css: '' };
  let mod = null;

  class FixedDate extends Date {
    constructor(...args) {
      if (args.length === 0) super(2026, 10, 9, hour, 0, 0);
      else super(...args);
    }
  }

  const sandbox = {
    window: { __ModuleLoader__: { load: (m) => { mod = m; } } },
    document: {
      createElement: () => ({ setAttribute() {}, set textContent(v) { captured.css = v; }, remove() {} }),
      head: { append() {} },
      body: { setAttribute() {}, removeAttribute() {} },
      addEventListener() {},
      removeEventListener() {},
    },
    Date: FixedDate,
    setInterval: () => 1,
    clearInterval: () => {},
    requestAnimationFrame: (fn) => 1,
    cancelAnimationFrame() {},
    console,
  };
  vm.runInNewContext(code, sandbox, { filename: 'client.js' });

  const react = fakeReact();
  const api = mod.factory((id) => (id === 'react' ? react : undefined));

  const ctx = {
    effect: (fn) => fn(),
    theme: { overrideTokens: (src, tokens) => { captured.tokens = tokens; return () => {}; } },
    slots: {
      inject: (key, cb) => { captured.slots.push({ key, ...cb() }); },
      register: (opts, comp) => ({ opts, comp }),
    },
    locale: {
      register: (ns, dicts) => { captured.locale = dicts; return () => {}; },
      bind: () => (k) => `«${k}»`,
    },
    get: () => undefined,
  };
  api.apply(ctx);
  return { api, captured, react };
}

function greetingText(hour) {
  const { captured, react } = run(hour);
  const slot = captured.slots.find((s) => s.key === 'sidebar.brand.name');
  const outer = slot.comp();
  const inner = outer.type(outer.props);
  return inner.children[0];
}

const morning = run(9);
console.log('inject:', morning.api.inject.join(', '));
console.log('slots:', morning.captured.slots.map((s) => `${s.key}[${s.opts.priority ?? 'default'}]`).join(' | '));

const mark = morning.captured.slots.find((s) => s.key === 'sidebar.brand.mark');
console.log('rail mark renders:', mark ? mark.comp({ size: 24 }) : 'MISSING');
const hero = morning.captured.slots.find((s) => s.key === 'conversation.hero.brand.mark');
const heroEl = hero ? hero.comp({ size: 48 }) : null;
console.log('hero mark:', heroEl && heroEl.type, heroEl && heroEl.props.width, heroEl && heroEl.props.className, heroEl && heroEl.props.src.slice(0, 26));
const dock = morning.captured.slots.find((s) => s.key === 'conversation.composer.dock');
console.log('dock id:', dock && dock.opts.id, 'order:', dock && dock.opts.order);

console.log('tokens has greeting size:', Boolean(morning.captured.tokens['--bmw-greeting-size']));
console.log('tokens has team tracking:', Boolean(morning.captured.tokens['--bmw-team-tracking']));
console.log('locale keys:', Object.keys(morning.captured.locale.en).join(', '));
console.log('css uppercase hero:', /data-phase="hero"\] \[class\*="headline"\]/.test(morning.captured.css));
console.log('css hides mark cell:', /\[class\*="brandMark"\]\s*\{\s*display:\s*none/.test(morning.captured.css));
console.log('greeting 09:', greetingText(9));
console.log('greeting 13:', greetingText(13));
console.log('greeting 21:', greetingText(21));
