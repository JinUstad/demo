"""
Pure Python PDF Generator for React Practice Notes (English Version)
Generates a multi-page, formatted PDF with headers, footers, code boxes,
and detailed comments explaining "Why is it used?" line-by-line for students.
"""

import os
import sys

class SimplePDF:
    def __init__(self, filename="React_Practice_Notes.pdf"):
        self.filename = filename
        self.pages = []
        self.current_stream = []
        self.width = 595.28  # A4 width in pt
        self.height = 841.89 # A4 height in pt
        self.margin_left = 40.0
        self.margin_right = 40.0
        self.margin_top = 45.0
        self.margin_bottom = 45.0
        self.content_width = self.width - self.margin_left - self.margin_right
        self.y = self.height - self.margin_top
        self.page_number = 0

    def start_new_page(self):
        if self.current_stream:
            self.pages.append("".join(self.current_stream))
            self.current_stream = []
        self.page_number += 1
        self.y = self.height - self.margin_top
        
        # Header banner line
        self.set_color(0.12, 0.35, 0.75) # Blue
        self.rect(self.margin_left, self.height - 30, self.content_width, 2, fill=True)
        
        # Header text
        self.set_font("Helvetica-Bold", 8)
        self.set_color(0.4, 0.4, 0.4)
        self.text(self.margin_left, self.height - 25, "REACT CORE PRACTICE NOTES - STUDENTS HANDBOOK")
        self.text(self.width - self.margin_right - 120, self.height - 25, "TOPIC GUIDE & CODE EXPLANATIONS")

        # Footer text and page number
        self.set_font("Helvetica", 8)
        self.text(self.margin_left, 25, "Handcrafted for React Students | Complete with 'Why Is It Used?' Line Comments")
        self.text(self.width - self.margin_right - 45, 25, f"Page {self.page_number}")
        self.set_color(0.85, 0.85, 0.85)
        self.rect(self.margin_left, 35, self.content_width, 1, fill=True)

    def check_space(self, needed):
        if self.y - needed < self.margin_bottom:
            self.start_new_page()

    def set_font(self, font_name, size):
        font_key = "/F1"
        if "Bold" in font_name and "Courier" not in font_name:
            font_key = "/F2"
        elif "Courier-Bold" in font_name:
            font_key = "/F4"
        elif "Courier" in font_name:
            font_key = "/F3"
        self.current_stream.append(f"{font_key} {size} Tf\n")

    def set_color(self, r, g, b):
        self.current_stream.append(f"{r:.3f} {g:.3f} {b:.3f} rg\n")
        self.current_stream.append(f"{r:.3f} {g:.3f} {b:.3f} RG\n")

    def rect(self, x, y, w, h, fill=True, stroke=False):
        op = "f" if fill and not stroke else "B" if fill and stroke else "S"
        self.current_stream.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re {op}\n")

    def escape_text(self, text):
        return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")

    def text(self, x, y, text):
        escaped = self.escape_text(text)
        self.current_stream.append(f"BT {x:.2f} {y:.2f} Td ({escaped}) Tj ET\n")

    def add_title_cover(self, title, subtitle):
        self.start_new_page()
        # Title background box
        self.set_color(0.12, 0.22, 0.45) # Deep navy blue
        self.rect(self.margin_left, self.y - 70, self.content_width, 70, fill=True)

        self.set_color(1.0, 1.0, 1.0)
        self.set_font("Helvetica-Bold", 17)
        self.text(self.margin_left + 15, self.y - 28, title)

        self.set_color(0.85, 0.92, 1.0)
        self.set_font("Helvetica", 10.5)
        self.text(self.margin_left + 15, self.y - 50, subtitle)
        self.y -= 85

    def add_section_header(self, number_str, title):
        self.check_space(60)
        self.y -= 10
        # Badge background
        self.set_color(0.15, 0.35, 0.75)
        self.rect(self.margin_left, self.y - 22, 32, 22, fill=True)
        self.set_color(1.0, 1.0, 1.0)
        self.set_font("Helvetica-Bold", 12)
        self.text(self.margin_left + 8, self.y - 16, number_str)

        # Title text
        self.set_color(0.1, 0.15, 0.25)
        self.set_font("Helvetica-Bold", 13.5)
        self.text(self.margin_left + 40, self.y - 16, title)

        # Underline
        self.y -= 26
        self.set_color(0.8, 0.85, 0.92)
        self.rect(self.margin_left, self.y, self.content_width, 1.5, fill=True)
        self.y -= 12

    def add_callout(self, title, items):
        height = 25 + (len(items) * 14)
        self.check_space(height + 15)
        
        box_y = self.y - height
        # Soft yellow / warm highlight
        self.set_color(0.98, 0.97, 0.90)
        self.rect(self.margin_left, box_y, self.content_width, height, fill=True)
        
        # Left border indicator
        self.set_color(0.85, 0.55, 0.10)
        self.rect(self.margin_left, box_y, 4, height, fill=True)

        # Callout Title
        self.set_color(0.70, 0.40, 0.05)
        self.set_font("Helvetica-Bold", 10)
        self.text(self.margin_left + 14, self.y - 14, title)

        curr_y = self.y - 28
        self.set_font("Helvetica", 8.5)
        self.set_color(0.2, 0.2, 0.2)
        for item in items:
            self.text(self.margin_left + 16, curr_y, f"- {item}")
            curr_y -= 13

        self.y = box_y - 12

    def add_paragraph(self, text, bold_prefix=""):
        self.set_font("Helvetica", 9)
        self.set_color(0.2, 0.2, 0.2)
        words = text.split(" ")
        line = bold_prefix
        lines = []
        for word in words:
            if len(line + " " + word) > 105:
                lines.append(line)
                line = word
            else:
                line = (line + " " + word) if line else word
        if line:
            lines.append(line)

        self.check_space(len(lines) * 13 + 5)
        for l in lines:
            self.text(self.margin_left, self.y, l)
            self.y -= 12
        self.y -= 4

    def add_code_block(self, code_lines):
        line_height = 11.5
        box_height = 18 + (len(code_lines) * line_height)
        self.check_space(box_height + 10)

        box_y = self.y - box_height
        # Dark code background
        self.set_color(0.12, 0.14, 0.18)
        self.rect(self.margin_left, box_y, self.content_width, box_height, fill=True)

        # Header bar for code box
        self.set_color(0.18, 0.21, 0.27)
        self.rect(self.margin_left, self.y - 16, self.content_width, 16, fill=True)
        self.set_font("Helvetica-Bold", 7.5)
        self.set_color(0.7, 0.75, 0.85)
        self.text(self.margin_left + 10, self.y - 12, "CODE SNIPPET - WITH 'WHY IS IT USED' COMMENTS")

        curr_y = self.y - 28
        for line in code_lines:
            trimmed = line.strip()
            if trimmed.startswith("//") or trimmed.startswith("/*") or "WHY" in line or "PURPOSE" in line:
                self.set_font("Courier-Bold", 8)
                self.set_color(0.40, 0.80, 0.45) # Green for comments
            elif any(k in line for k in ["const", "function", "return", "export", "import", "if", "useState"]):
                self.set_font("Courier", 8)
                self.set_color(0.95, 0.75, 0.35) # Gold/yellow for keywords
            else:
                self.set_font("Courier", 8)
                self.set_color(0.90, 0.93, 0.98) # Light text

            display_line = line[:100]
            self.text(self.margin_left + 10, curr_y, display_line)
            curr_y -= line_height

        self.y = box_y - 15

    def save(self):
        if self.current_stream:
            self.pages.append("".join(self.current_stream))
            self.current_stream = []

        total_pages = len(self.pages)
        cat_id = 1
        pages_id = 2
        first_page_id = 3
        first_stream_id = first_page_id + total_pages
        font_f1 = first_stream_id + total_pages
        font_f2 = font_f1 + 1
        font_f3 = font_f2 + 1
        font_f4 = font_f3 + 1
        total_objects = font_f4

        obj_strings = {}
        obj_strings[cat_id] = f"{cat_id} 0 obj\n<< /Type /Catalog /Pages {pages_id} 0 R >>\nendobj\n"

        kids = " ".join([f"{first_page_id + i} 0 R" for i in range(total_pages)])
        obj_strings[pages_id] = f"{pages_id} 0 obj\n<< /Type /Pages /Kids [{kids}] /Count {total_pages} >>\nendobj\n"

        for i in range(total_pages):
            p_id = first_page_id + i
            s_id = first_stream_id + i
            obj_strings[p_id] = (
                f"{p_id} 0 obj\n"
                f"<< /Type /Page /Parent {pages_id} 0 R\n"
                f"   /MediaBox [0 0 {self.width:.2f} {self.height:.2f}]\n"
                f"   /Contents {s_id} 0 R\n"
                f"   /Resources <<\n"
                f"     /Font <<\n"
                f"       /F1 {font_f1} 0 R\n"
                f"       /F2 {font_f2} 0 R\n"
                f"       /F3 {font_f3} 0 R\n"
                f"       /F4 {font_f4} 0 R\n"
                f"     >>\n"
                f"   >>\n"
                f">>\nendobj\n"
            )

        for i in range(total_pages):
            s_id = first_stream_id + i
            stream_data = self.pages[i]
            stream_len = len(stream_data.encode("latin-1", errors="replace"))
            obj_strings[s_id] = (
                f"{s_id} 0 obj\n"
                f"<< /Length {stream_len} >>\n"
                f"stream\n"
                f"{stream_data}"
                f"endstream\nendobj\n"
            )

        obj_strings[font_f1] = f"{font_f1} 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n"
        obj_strings[font_f2] = f"{font_f2} 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>\nendobj\n"
        obj_strings[font_f3] = f"{font_f3} 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Courier >>\nendobj\n"
        obj_strings[font_f4] = f"{font_f4} 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Courier-Bold >>\nendobj\n"

        output = ["%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"]
        xref_offsets = [0]
        current_offset = len(output[0].encode("latin-1"))

        for i in range(1, total_objects + 1):
            xref_offsets.append(current_offset)
            data_bytes = obj_strings[i].encode("latin-1", errors="replace")
            output.append(obj_strings[i])
            current_offset += len(data_bytes)

        xref_start = current_offset
        output.append(f"xref\n0 {total_objects + 1}\n")
        output.append("0000000000 65535 f \n")
        for i in range(1, total_objects + 1):
            output.append(f"{xref_offsets[i]:010d} 00000 n \n")

        output.append(
            f"trailer\n<< /Size {total_objects + 1} /Root {cat_id} 0 R >>\n"
            f"startxref\n{xref_start}\n%%EOF\n"
        )

        final_content = "".join(output).encode("latin-1", errors="replace")
        with open(self.filename, "wb") as f:
            f.write(final_content)
        print(f"Generated PDF: {self.filename} ({len(final_content)} bytes, {total_pages} pages)")


def generate_react_practice_notes(out_path):
    pdf = SimplePDF(out_path)
    
    # COVER / HEADER
    pdf.add_title_cover("React Core Concepts - Student Practice Handbook", "Complete 6 Topics with 'Why Is It Used?' Line-by-Line Code Explanations")

    pdf.add_paragraph("Welcome students! This handbook covers 6 foundational React topics essential for interviews and real-world project development. Every single code line contains explicit comments explaining WHY that pattern or syntax is used, giving you total clarity on React concepts.")

    # -------------------------------------------------------------
    # TOPIC 1: PROPS
    # -------------------------------------------------------------
    pdf.add_section_header("1", "Props (Properties) in React")
    pdf.add_paragraph("Props (short for Properties) are the fundamental mechanism in React for transferring data and callback functions from a Parent component down to a Child component. Props are strictly read-only (immutable).")
    
    pdf.add_callout("WHY IS IT USED? (Purpose & Benefits of Props)", [
        "Dynamic Rendering: Reusing a single component (e.g. Card, Button) to display thousands of different user records.",
        "Unidirectional Data Flow: Data always travels downward (Parent -> Child), ensuring predictable state and easy debugging.",
        "Callback Execution: Parents can pass functions as props so child components can trigger parent events on user interaction."
    ])

    pdf.add_code_block([
        "// 1. CHILD COMPONENT: Receives and renders props",
        "// [WHY IS IT USED?]: Object destructuring provides direct variable access without repetitive 'props.name'",
        "// [WHY IS IT USED?]: Default value 'Student' prevents UI breaks if parent forgets to pass the role prop",
        "function UserCard({ name, role = 'Student', isOnline, onNotify }) {",
        "  return (",
        "    <div className='card p-3 shadow-sm'>",
        "      {/* [WHY]: Displays dynamic data supplied by the parent */} ",
        "      <h5>Name: {name}</h5>",
        "      <p className='text-muted'>Role: {role}</p>",
        "      {/* [WHY]: Conditional rendering: dynamically switches badge color based on online boolean */} ",
        "      <span className={isOnline ? 'badge bg-success' : 'badge bg-secondary'}>",
        "        {isOnline ? 'Active Now' : 'Offline'}",
        "      </span>",
        "      {/* [WHY]: Executes callback prop to inform parent when button is clicked */} ",
        "      <button onClick={() => onNotify(name)}>Notify Parent</button>",
        "    </div>",
        "  );",
        "}",
        "",
        "// 2. PARENT COMPONENT: Holds state and passes props down",
        "function App() {",
        "  const handleNotification = (studentName) => alert('Notified: ' + studentName);",
        "  return (",
        "    <div>",
        "      {/* [WHY]: Passing distinct custom attributes to configure reusable UserCard instances */} ",
        "      <UserCard name='Alex Rivera' role='Frontend Engineer' isOnline={true} onNotify={handleNotification} />",
        "      <UserCard name='Sara Connor' role='UI/UX Designer' isOnline={false} onNotify={handleNotification} />",
        "    </div>",
        "  );",
        "}"
    ])

    # -------------------------------------------------------------
    # TOPIC 2: PROPS DRILLING
    # -------------------------------------------------------------
    pdf.add_section_header("2", "Props Drilling (Problem & Context API Solution)")
    pdf.add_paragraph("Props Drilling occurs when data must be passed from a top Parent to a deeply nested Child, forcing all intermediate components to accept and forward props they do not use or care about.")

    pdf.add_callout("WHY IS IT IMPORTANT TO UNDERSTAND? (Issues & Modern Solutions)", [
        "Unnecessary Boilerplate: Intermediate components are forced to declare props purely to pass them forward.",
        "Refactoring Fragility: Renaming or restructuring a prop requires editing every single file along the tree.",
        "Context API Solution: For 1-2 levels, props drilling is harmless. For deeply nested or global state, React Context API is the best practice."
    ])

    pdf.add_code_block([
        "// ========================================================================",
        "// THE MODERN SOLUTION: REACT CONTEXT API (No Props Drilling)",
        "// ========================================================================",
        "import { createContext, useContext, useState } from 'react';",
        "",
        "// [WHY IS IT USED?]: Creates a global Context object for direct child consumption",
        "const ThemeContext = createContext();",
        "",
        "function GrandParent() {",
        "  const [theme, setTheme] = useState('dark-theme');",
        "  return (",
        "    // [WHY]: Provider makes 'theme' accessible to any descendant component without passing props",
        "    <ThemeContext.Provider value={{ theme }}>",
        "      <MiddleComponent />",
        "    </ThemeContext.Provider>",
        "  );",
        "}",
        "",
        "// [WHY CLEAN]: MiddleComponent receives ZERO props and remains completely decoupled",
        "function MiddleComponent() {",
        "  return <DeepChild />;",
        "}",
        "",
        "function DeepChild() {",
        "  // [WHY IS IT USED?]: useContext hook extracts the data directly from the Provider",
        "  const { theme } = useContext(ThemeContext);",
        "  return <span className='badge bg-dark'>Active Theme: {theme}</span>;",
        "}"
    ])

    # -------------------------------------------------------------
    # TOPIC 3: FORM HANDLING IN REACT
    # -------------------------------------------------------------
    pdf.add_section_header("3", "Form Handling in React")
    pdf.add_paragraph("In traditional HTML, submitting a form triggers a full page reload. In React Single Page Applications (SPAs), we prevent browser reloads and manage all inputs via React State.")

    pdf.add_callout("WHY IS IT USED? (Key React Form Mechanics)", [
        "e.preventDefault(): Halts browser default reload behavior so React state and application memory remain intact.",
        "Single Centralized State: Storing form fields in a single state object prevents declaring multiple useState calls.",
        "Dynamic [e.target.name]: Uses ES6 computed property names so a single handleChange function scales across 20+ inputs."
    ])

    pdf.add_code_block([
        "import { useState } from 'react';",
        "",
        "function StudentRegistrationForm() {",
        "  // [WHY IS IT USED?]: Centralized object state keeps all form fields organized in one place",
        "  const [formData, setFormData] = useState({ fullName: '', email: '', course: 'React' });",
        "",
        "  // [WHY IS IT USED?]: Universal change handler using dynamic property key computation",
        "  const handleChange = (e) => {",
        "    const { name, value } = e.target;",
        "    // [WHY]: Spread operator (...) preserves existing fields while updating the target field",
        "    setFormData((prev) => ({ ...prev, [name]: value }));",
        "  };",
        "",
        "  const handleSubmit = (e) => {",
        "    // [WHY]: Halts browser page reload to maintain Single Page Application (SPA) state",
        "    e.preventDefault();",
        "    console.log('Sending JSON payload to backend:', formData);",
        "    alert('Registration successful for: ' + formData.fullName);",
        "  };",
        "",
        "  return (",
        "    <form onSubmit={handleSubmit}>",
        "      {/* [WHY]: name attribute matches the state key in handleChange */}",
        "      <input name='fullName' value={formData.fullName} onChange={handleChange} placeholder='Full Name' />",
        "      <input name='email' type='email' value={formData.email} onChange={handleChange} placeholder='Email' />",
        "      <button type='submit'>Register Student</button>",
        "    </form>",
        "  );",
        "}"
    ])

    # -------------------------------------------------------------
    # TOPIC 4: FORM VALIDATION
    # -------------------------------------------------------------
    pdf.add_section_header("4", "Form Validation in React")
    pdf.add_paragraph("Client-side validation verifies that user inputs follow critical business requirements (such as non-empty fields, valid email structures, and minimum password lengths) before transmission to the server.")

    pdf.add_callout("WHY IS IT USED? (Why Client-Side Validation is Essential)", [
        "Instant User Guidance: Immediately notifies the user of syntax or length mistakes without waiting for an API response.",
        "Clean Database Ingestion: Prevents malformed, incomplete, or malicious data from reaching the backend.",
        "onBlur + Touched State: Delays error alerts until the user finishes typing and leaves the input (Best UX practice)."
    ])

    pdf.add_code_block([
        "function ValidatedSignup() {",
        "  const [email, setEmail] = useState('');",
        "  // [WHY IS IT USED?]: Separate error state stores specific validation messages dynamically",
        "  const [error, setError] = useState('');",
        "",
        "  const validateEmail = (val) => {",
        "    // [WHY]: Regular expression test validates presence of '@' and a valid top-level domain",
        "    const regex = /^\\S+@\\S+\\.\\S+$/;",
        "    if (!val.trim()) return 'Email is required (cannot be empty)';",
        "    if (!regex.test(val)) return 'Invalid email format (e.g. name@domain.com)';",
        "    return '';",
        "  };",
        "",
        "  const handleBlur = () => {",
        "    // [WHY]: onBlur fires when cursor leaves input - ideal time to display validation feedback",
        "    setError(validateEmail(email));",
        "  };",
        "",
        "  const handleSubmit = (e) => {",
        "    e.preventDefault();",
        "    const err = validateEmail(email);",
        "    if (err) {",
        "      setError(err); // [WHY]: Aborts submission because validation requirements failed",
        "      return;",
        "    }",
        "    alert('Validation Passed! Processing request...');",
        "  };",
        "",
        "  return (",
        "    <form onSubmit={handleSubmit}>",
        "      {/* [WHY]: Dynamic CSS class highlights input border in red if error exists */}",
        "      <input className={error ? 'border-danger' : 'border-success'}",
        "             value={email} onChange={(e) => { setEmail(e.target.value); setError(''); }}",
        "             onBlur={handleBlur} placeholder='student@school.com' />",
        "      {/* [WHY]: Conditional rendering displays error badge only when an error is present */}",
        "      {error && <span style={{ color: 'red', fontSize: '12px' }}>{error}</span>}",
        "      <button type='submit'>Verify & Submit</button>",
        "    </form>",
        "  );",
        "}"
    ])

    # -------------------------------------------------------------
    # TOPIC 5: REUSABLE COMPONENTS
    # -------------------------------------------------------------
    pdf.add_section_header("5", "Reusable Components (DRY Principle)")
    pdf.add_paragraph("A Reusable Component is a modular, self-contained piece of UI crafted with flexible props and children so it can be deployed throughout an entire application without duplicating code.")

    pdf.add_callout("WHY IS IT USED? (Why Reusability is React's Superpower)", [
        "DRY Principle (Don't Repeat Yourself): Eliminates redundant HTML and copy-pasted CSS classes across pages.",
        "Centralized Maintenance: Updating button border-radius or padding in 1 file instantly updates all 50 occurrences.",
        "The children Prop: Enables maximum flexibility to pass custom text, icons, and nested JSX inside the component."
    ])

    pdf.add_code_block([
        "// Custom Reusable Button Component",
        "// [WHY IS IT USED?]: Props (variant, size, children) allow universal styling across the whole app",
        "function AppButton({ variant = 'primary', size = 'md', isPill = false, onClick, children }) {",
        "  // [WHY]: Template literals dynamically generate appropriate Bootstrap classes",
        "  const sizeClass = size === 'sm' ? 'btn-sm' : size === 'lg' ? 'btn-lg' : '';",
        "  const shapeClass = isPill ? 'rounded-pill' : 'rounded-3';",
        "",
        "  return (",
        "    <button",
        "      className={`btn btn-${variant} ${sizeClass} ${shapeClass} fw-bold m-1`}",
        "      onClick={onClick}   // [WHY]: Executes parent action dynamically",
        "      type='button'",
        "    >",
        "      {/* [WHY]: 'children' prop accepts any nested text, icon components, or badges */}",
        "      {children}",
        "    </button>",
        "  );",
        "}",
        "",
        "// Usage examples across different pages:",
        "function Dashboard() {",
        "  return (",
        "    <div>",
        "      {/* [WHY]: Primary pill button without re-writing button CSS */}",
        "      <AppButton variant='primary' size='sm' isPill={true} onClick={() => alert('Saved!')}>",
        "        Save Changes",
        "      </AppButton>",
        "      {/* [WHY]: Danger variant using the exact same underlying component */}",
        "      <AppButton variant='danger' size='lg' onClick={() => alert('Deleted!')}>",
        "        Delete Account",
        "      </AppButton>",
        "    </div>",
        "  );",
        "}"
    ])

    # -------------------------------------------------------------
    # TOPIC 6: CONTROLLED COMPONENTS
    # -------------------------------------------------------------
    pdf.add_section_header("6", "Controlled Components")
    pdf.add_paragraph("A Controlled Component is an input element whose value is entirely governed by React State rather than the DOM. Formula: value={state} + onChange={(e) => setState(e.target.value)}.")

    pdf.add_callout("WHY IS IT USED? (Why Controlled over Uncontrolled?)", [
        "Single Source of Truth: The displayed value in the DOM and React State are always 100% synchronized.",
        "Live Data Transformations: Allows real-time uppercase conversion, phone number masking, and character limits as the user types.",
        "Programmatic Control: Inputs can be instantly cleared or pre-filled with demo data by updating state, with zero DOM manipulation."
    ])

    pdf.add_code_block([
        "function ControlledInputDemo() {",
        "  // [WHY IS IT USED?]: State variable acts as the absolute 'Single Source of Truth'",
        "  const [text, setText] = useState('');",
        "",
        "  return (",
        "    <div className='p-3 border rounded'>",
        "      <label>Controlled Live Transformer:</label>",
        "      <input",
        "        type='text'",
        "        // [WHY]: value={text} forces the input to be completely driven by React state",
        "        value={text}",
        "        // [WHY]: onChange updates state on every keystroke, transforming input to UPPERCASE in real time",
        "        onChange={(e) => setText(e.target.value.toUpperCase())}",
        "        placeholder='Type in lowercase, see uppercase live...'",
        "      />",
        "",
        "      {/* [WHY]: Live state verification displays synchronized value */}",
        "      <p>Current State Value: <strong>{text}</strong></p>",
        "      <p>Length: {text.length} / 50 characters</p>",
        "",
        "      {/* [WHY]: Programmatic reset directly updates state without querying the DOM */}",
        "      <button onClick={() => setText('')}>Clear Input via State</button>",
        "    </div>",
        "  );",
        "}"
    ])

    # Summary table / Student Quick Revision
    pdf.add_section_header("Summary", "Quick Student Reference Cheatsheet")
    pdf.add_paragraph("1. Props: Unidirectional Parent-to-Child data passing. Read-only (immutable).")
    pdf.add_paragraph("2. Props Drilling: Passing props through intermediate layers that do not need them. Solution: React Context API.")
    pdf.add_paragraph("3. Forms: Controlled via e.preventDefault() and state to deliver seamless SPA behavior.")
    pdf.add_paragraph("4. Form Validation: Validating client input rules before submission to ensure data integrity and superior UX.")
    pdf.add_paragraph("5. Reusable Component: Building modular, DRY UI blocks parameterized via props and the children prop.")
    pdf.add_paragraph("6. Controlled Component: value + onChange combo binding the DOM input directly to React state.")

    pdf.save()


if __name__ == "__main__":
    out = "public/React_Practice_Notes.pdf"
    if len(sys.argv) > 1:
        out = sys.argv[1]
    generate_react_practice_notes(out)
    generate_react_practice_notes("React_Practice_Notes.pdf")
