import { useState } from 'react'

// 1. REUSABLE COMPONENT: A button that takes 'text', 'color', and 'onClick'
function MyButton({ text, color = 'primary', onClick }) {
    return (
        <button type="button" className={`btn btn-${color} m-1`} onClick={onClick}>
            {text}
        </button>
    )
}

function ReusableComponentDemo() {
    const [action, setAction] = useState('Click any button below to test')

    return (
        <div>
            <div className="card p-3 mb-3 shadow-sm">
                <h5 className="fw-bold mb-2">Reusable Component in Action</h5>
                <p className="text-muted small mb-3">
                    One single <code>&lt;MyButton /&gt;</code> component reused 3 times with different props:
                </p>

                {/* Reusing the same component with different props */}
                <div className="d-flex flex-wrap gap-2 mb-3">
                    <MyButton
                        text="Primary Action (Save)"
                        color="primary"
                        onClick={() => setAction('You clicked Save (Primary)')}
                    />
                    <MyButton
                        text="Success Action (Submit)"
                        color="success"
                        onClick={() => setAction('You clicked Submit (Success)')}
                    />
                    <MyButton
                        text="Danger Action (Delete)"
                        color="danger"
                        onClick={() => setAction('You clicked Delete (Danger)')}
                    />
                </div>

                <div className="alert alert-secondary mb-0 py-2">
                    <strong>Result:</strong> {action}
                </div>
            </div>

            {/* Simple Code */}
            <div className="bg-dark text-white p-3 rounded small font-monospace">
                <div className="text-warning mb-1">// Reusable Component Concept:</div>
                <pre className="m-0 text-light" style={{ whiteSpace: 'pre-wrap' }}>
{`// 1. Define once
function MyButton({ text, color, onClick }) {
  return <button className={"btn btn-" + color} onClick={onClick}>{text}</button>;
}

// 2. Reuse anywhere with different props
function App() {
  return (
    <div>
      <MyButton text="Save" color="success" onClick={() => alert("Saved")} />
      <MyButton text="Delete" color="danger" onClick={() => alert("Deleted")} />
    </div>
  );
}`}
                </pre>
            </div>
        </div>
    )
}

export default ReusableComponentDemo
