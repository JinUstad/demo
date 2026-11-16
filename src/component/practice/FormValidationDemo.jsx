import { useState } from 'react'

function FormValidationDemo() {
    const [username, setUsername] = useState('')
    const [error, setError] = useState('')
    const [success, setSuccess] = useState('')

    const handleSubmit = (e) => {
        e.preventDefault()

        // Simple validation check
        if (!username.trim()) {
            setError('Error: Username cannot be empty!')
            setSuccess('')
        } else if (username.length < 3) {
            setError('Error: Username must be at least 3 characters long!')
            setSuccess('')
        } else {
            setError('')
            setSuccess(`Success: "${username}" is valid and submitted!`)
        }
    }

    return (
        <div>
            <div className="card p-3 mb-3 shadow-sm">
                <h5 className="fw-bold mb-3">Simple Form Validation</h5>

                <form onSubmit={handleSubmit}>
                    <div className="mb-2">
                        <label className="form-label small fw-bold">Username (Min 3 characters):</label>
                        <input
                            type="text"
                            className={`form-control ${error ? 'is-invalid border-danger' : success ? 'is-valid border-success' : ''}`}
                            placeholder="Type username..."
                            value={username}
                            onChange={(e) => {
                                setUsername(e.target.value)
                                setError('')
                                setSuccess('')
                            }}
                        />
                    </div>

                    {/* Error display */}
                    {error && <div className="text-danger small fw-bold mb-2">{error}</div>}
                    {/* Success display */}
                    {success && <div className="text-success small fw-bold mb-2">{success}</div>}

                    <button type="submit" className="btn btn-danger">
                        Validate & Submit
                    </button>
                </form>
            </div>

            {/* Simple Code */}
            <div className="bg-dark text-white p-3 rounded small font-monospace">
                <div className="text-warning mb-1">// Simple Validation Logic:</div>
                <pre className="m-0 text-light" style={{ whiteSpace: 'pre-wrap' }}>
{`function ValidationExample() {
  const [name, setName] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (name.length < 3) {
      setError("Name must be at least 3 characters!");
    } else {
      setError("");
      alert("Valid name submitted!");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <button type="submit">Submit</button>
    </form>
  );
}`}
                </pre>
            </div>
        </div>
    )
}

export default FormValidationDemo
