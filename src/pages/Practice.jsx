import { useState } from 'react'
import PropsDemo from '../component/practice/PropsDemo'
import PropsDrillingDemo from '../component/practice/PropsDrillingDemo'
import FormDemo from '../component/practice/FormDemo'
import FormValidationDemo from '../component/practice/FormValidationDemo'
import ReusableComponentDemo from '../component/practice/ReusableComponentDemo'
import ControlledComponentDemo from '../component/practice/ControlledComponentDemo'

function Practice() {
    const [activeTab, setActiveTab] = useState('props')

    const tabs = [
        { id: 'props', label: '1. Props' },
        { id: 'props-drilling', label: '2. Props Drilling' },
        { id: 'form', label: '3. Form' },
        { id: 'form-validation', label: '4. Form Validation' },
        { id: 'reusable-component', label: '5. Reusable Component' },
        { id: 'controlled-component', label: '6. Controlled Component' }
    ]

    return (
        <main className="container py-4" style={{ maxWidth: '900px' }}>
            {/* Header */}
            <div className="mb-4 pb-3 border-bottom">
                <h2 className="fw-bold mb-1">React Practice Topics</h2>
                <p className="text-muted small mb-0">Direct working examples for each topic</p>
            </div>

            {/* Simple Bootstrap Tabs */}
            <ul className="nav nav-pills mb-4 gap-2 flex-wrap">
                {tabs.map((tab) => (
                    <li className="nav-item" key={tab.id}>
                        <button
                            type="button"
                            className={`nav-link fw-semibold ${activeTab === tab.id ? 'active' : 'bg-light text-dark'}`}
                            onClick={() => setActiveTab(tab.id)}
                        >
                            {tab.label}
                        </button>
                    </li>
                ))}
            </ul>

            {/* Active Tab Working Demo */}
            <div>
                {activeTab === 'props' && <PropsDemo />}
                {activeTab === 'props-drilling' && <PropsDrillingDemo />}
                {activeTab === 'form' && <FormDemo />}
                {activeTab === 'form-validation' && <FormValidationDemo />}
                {activeTab === 'reusable-component' && <ReusableComponentDemo />}
                {activeTab === 'controlled-component' && <ControlledComponentDemo />}
            </div>
        </main>
    )
}

export default Practice
