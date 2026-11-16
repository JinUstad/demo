import { useState } from 'react'

function ControlledComponentDemo() {
    // 1. React State is the single source of truth
    const [text, setText] = useState('')

    return (
        <div>
            <div className="card p-3 mb-3 shadow-sm">
                <h5 className="fw-bold mb-2">Controlled Component</h5>
                <p className="text-muted small mb-3">
                    Input is bound to React State: <code>value=&#123;text&#125;</code> and <code>onChange=&#123;(e) =&gt; setText(e.target.value)&#125;</code>
                </p>

                <div className="mb-3">
                    <label className="form-label small fw-bold">Controlled Input:</label>
                    <input
                        type="text"
                        className="form-control"
                        placeholder="Type anything here..."
                        value={text}
                        onChange={(e) => setText(e.target.value)}
                    />
                </div>

                <div className="p-3 bg-light border rounded mb-3">
                    <strong>Live Value in React State:</strong>{' '}
                    <span className="text-primary fw-bold">{text || '(empty)'}</span>
                </div>

                <button
                    type="button"
                    className="btn btn-outline-secondary btn-sm"
                    onClick={() => setText('')}
                >
                    Clear Input (via State)
                </button>
            </div>

            {/* Simple Code */}
            <div className="bg-dark text-white p-3 rounded small font-monospace">
                <div className="text-warning mb-1">// Controlled Component Pattern:</div>
                <pre className="m-0 text-light" style={{ whiteSpace: 'pre-wrap' }}>
{`function ControlledInput() {
  const [text, setText] = useState('');

  return (
    <div>
      {/* State controls the input value directly */}
      <input value={text} onChange={(e) => setText(e.target.value)} />
      <p>Typed: {text}</p>
      <button onClick={() => setText('')}>Clear</button>
    </div>
  );
}`}
                </pre>
            </div>
        </div>
    )
}

export default ControlledComponentDemo
