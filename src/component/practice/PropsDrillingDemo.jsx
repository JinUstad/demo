import { useState } from 'react'

// Level 3: Bottom Child (Actually needs the data)
function BottomChild({ message }) {
    return (
        <div className="p-3 border rounded bg-success-subtle border-success mt-2">
            <h6 className="fw-bold text-success mb-1">Level 3: Bottom Child (Final Destination)</h6>
            <p className="mb-0">
                Displaying Data: <strong>&quot;{message}&quot;</strong>
            </p>
        </div>
    )
}

// Level 2: Middle Component (Does NOT need the data, only forwards it)
function MiddleComponent({ message }) {
    return (
        <div className="p-3 border rounded bg-warning-subtle border-warning mt-2">
            <h6 className="fw-bold text-dark mb-1">Level 2: Middle Component (Passing Through)</h6>
            <p className="small text-muted mb-2">
                I don&apos;t use <code>message</code>, but I am forced to pass it to BottomChild!
            </p>
            <BottomChild message={message} />
        </div>
    )
}

// Level 1: Top Parent
function PropsDrillingDemo() {
    const [message, setMessage] = useState('Hello from Parent!')

    return (
        <div>
            <div className="card p-3 mb-3 shadow-sm">
                <h5 className="fw-bold mb-2">Level 1: Top Parent Component</h5>
                <label className="form-label small fw-bold">Change Message:</label>
                <input
                    type="text"
                    className="form-control mb-3"
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                />

                {/* Drilling starts here */}
                <MiddleComponent message={message} />
            </div>

            {/* Simple Code */}
            <div className="bg-dark text-white p-3 rounded small font-monospace">
                <div className="text-warning mb-1">// Props Drilling Concept:</div>
                <pre className="m-0 text-light" style={{ whiteSpace: 'pre-wrap' }}>
                    {`// Parent passes to Middle -> Middle passes to Bottom
function Parent() {
  const [data, setData] = useState("Hello");
  return <Middle data={data} />;
}

function Middle({ data }) {
  // Middle doesn't need data, but must pass it down
  return <Bottom data={data} />;
}

function Bottom({ data }) {
  return <h1>{data}</h1>;
}`}
                </pre>
            </div>
        </div>
    )
}

export default PropsDrillingDemo
