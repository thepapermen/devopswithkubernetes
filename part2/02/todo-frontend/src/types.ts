export interface TodoIn {
  txt: string
}

export interface TodoOut {
  id: number
  txt: string
  created_at: string
}

export interface TodoList {
  items: TodoOut[],
  count: number
}

