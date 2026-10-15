erDiagram
    teachers ||--o{ lessons : teaches
    instruments ||--o{ lessons : used_in
    teachers ||--o{ teacher_instruments : has
    instruments ||--o{ teacher_instruments : taught_by
    students ||--o{ lesson_students : attends
    lessons ||--o{ lesson_students : includes