import { useState } from 'react'

function FormDemo() {
    const [name, setName] = useState('')
    const [email, setEmail] = useState('')
    const [number, setNumber] = useState('')
    const [submitted, setSubmitted] = useState(null)

    const handleSubmit = (e) => {
        e.preventDefault() // Prevents page reload!
        setSubmitted({ name, email, number })
    }

    return (
        <div>
            <div className="card p-3 mb-3 shadow-sm">
                <h5 className="fw-bold mb-3">Simple React Form</h5>

                <form onSubmit={handleSubmit}>
                    <div className="mb-2">
                        <label className="form-label small fw-bold">Name:</label>
                        <input
                            type="text"
                            className="form-control"
                            placeholder="Enter your name"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                            required
                        />
                    </div>

                    <div className="mb-3">
                        <label className="form-label small fw-bold">Email:</label>
                        <input
                            type="email"
                            className="form-control"
                            placeholder="Enter your email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </div>
                    <div className="mb-3">
                        <label className="form-label small fw-bold">Number:</label>
                        <input
                            type="number"
                            className="form-control"
                            placeholder="Enter your email"
                            value={number}
                            onChange={(e) => setNumber(e.target.value)}
                            required
                        />
                    </div>

                    <button type="submit" className="btn btn-primary">
                        Submit Form (e.preventDefault)
                    </button>
                </form>

                {/* Output shown without page reload */}
                {submitted && (
                    <div className="alert alert-success mt-3 mb-0">
                        <strong>Form Submitted! (Page did not reload):</strong>
                        <div>Name: {submitted.name}</div>
                        <div>Email: {submitted.email}</div>
                        <div>Email: {submitted.number}</div>
                    </div>
                )}
            </div>

            {/* Simple Code */}
            <div className="bg-dark text-white p-3 rounded small font-monospace">
                <div className="text-warning mb-1">// Simple Form Handling:</div>
                <pre className="m-0 text-light" style={{ whiteSpace: 'pre-wrap' }}>
                    {`function FormExample() {
  const [name, setName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault(); // [WHY]: Stops browser page refresh
    alert("Submitted name: " + name);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <button type="submit">Submit</button>
    </form>
  );
}`}
                </pre>
            </div>
        </div>
    )
}

export default FormDemo
