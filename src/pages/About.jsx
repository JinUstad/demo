import { useState } from 'react'

function About() {

    // fisrt empty state for the input value and items list
    const [value, setValue] = useState('')

    // second step when i enter any value save inside the array and show in the list
    const [items, setItems] = useState([])

    function handleSubmit(event) {
        event.preventDefault()
        const newItem = value.trim()

        if (!newItem) return

        setItems((currentItems) => [...currentItems, newItem])
        setValue('')
    }

    function handleDelete(itemIndex) {
        setItems((currentItems) => currentItems.filter((_, index) => index !== itemIndex))
    }

    return (
        <main className="container py-5">
            <h1>About Us</h1>
            <p>Learn more about our project and what we do.</p>

            <form className="d-flex align-items-end gap-2 mb-4" onSubmit={handleSubmit}>
                <div className="flex-grow-1">
                    <label className="form-label" htmlFor="about-item">Add an item</label>
                    <input
                        className="form-control"
                        id="about-item"
                        onChange={(e) => setValue(e.target.value)}
                        placeholder="Enter a value"
                        value={value}
                    />
                </div>
                <button className="btn btn-primary" type="submit" >
                    Add
                </button>
            </form>
            {/* <h1>{value}</h1> */}
            {items.length === 0 ? (
                <p>No items yet.</p>
            ) : (
                <ul className="list-group">
                    {items.map((item, index) => (
                        <li className="list-group-item d-flex align-items-center justify-content-between gap-3" key={index}>
                            <span>{item}</span>
                            <button
                                className="btn btn-outline-danger btn-sm"
                                onClick={() => handleDelete(index)}
                                type="button"
                            >
                                Delete
                            </button>
                        </li>
                    ))}
                </ul>
            )}
        </main>
    )
}

export default About
