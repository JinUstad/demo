import { useState } from 'react'

// 1. CHILD COMPONENT: Receives 'name' and 'role' via props
function ChildComponent({ name, role }) {
    return (
        <div className="p-3 border rounded bg-light">
            <h5 className="text-primary mb-1">Child Component</h5>
            <p className="mb-0">
                Received Props: <strong>Name:</strong> {name || '(empty)'} | <strong>Role:</strong> {role}
            </p>
        </div>
    )
}

// 2. PARENT COMPONENT: Holds state and passes it to Child as props
function PropsDemo() {
    const [name, setName] = useState('Rahul')
    const [role, setRole] = useState('Frontend Developer')

    return (
        <div>
            <div className="card p-3 mb-3 shadow-sm">
                <h5 className="fw-bold mb-3">Parent Component (Controls the Data)</h5>
                
                <div className="row g-2 mb-3">
                    <div className="col-md-6">
                        <label className="form-label small fw-bold">Type Name:</label>
                        <input
                            type="text"
                            className="form-control"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                        />
                    </div>
                    <div className="col-md-6">
                        <label className="form-label small fw-bold">Select Role:</label>
                        <select className="form-select" value={role} onChange={(e) => setRole(e.target.value)}>
                            <option value="Frontend Developer">Frontend Developer</option>
                            <option value="Backend Developer">Backend Developer</option>
                            <option value="UI/UX Designer">UI/UX Designer</option>
                        </select>
                    </div>
                </div>

                {/* Passing props to Child */}
                <ChildComponent name={name} role={role} />
            </div>

            {/* Simple Code */}
            <div className="bg-dark text-white p-3 rounded small font-monospace">
                <div className="text-warning mb-1">// Simple Working Code:</div>
                <pre className="m-0 text-light" style={{ whiteSpace: 'pre-wrap' }}>
{`// 1. Child receives props
function ChildComponent({ name, role }) {
  return <h3>Hello, {name} - Role: {role}</h3>;
}

// 2. Parent sends props
function Parent() {
  const [name, setName] = useState('Rahul');
  return <ChildComponent name={name} role="Frontend Developer" />;
}`}
                </pre>
            </div>
        </div>
    )
}

export default PropsDemo
