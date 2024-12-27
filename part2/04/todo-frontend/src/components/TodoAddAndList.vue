<script setup lang="ts">
import { useMutation, useQuery, useQueryClient } from '@tanstack/vue-query'
import { type TodoOut, type TodoIn, type TodoList } from '@/types.ts'
import axios from 'axios'
import { ref } from 'vue'

const todoApiUrl:string = import.meta.env.VITE_API_ROOT_URL
const imageUrl = import.meta.env.VITE_IMAGE_BACKEND_URL

const queryClient = useQueryClient()
const { isPending, isFetching, isError, data: todos, error } = useQuery({
  queryKey: ['todos'],
  queryFn: ()=> axios.get<TodoList>(todoApiUrl),
  select: (response) => response.data
})

const todo_txt = ref('')

const mutation = useMutation({
  mutationFn: (variables: TodoIn) => axios.post<TodoOut>(todoApiUrl, variables),
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ['todos'] })
  },
})

function createTodo() {
  mutation.mutate({
    txt: todo_txt.value,
  })
  todo_txt.value = ''
}

</script>

<template>
  <main>
    <img alt="Vue logo" class="random-img" :src="imageUrl" width="125" height="125" />
    <div>
        <form @submit.prevent="createTodo()">
          <input v-model="todo_txt">
          <button>Add Todo</button>
        </form>
    </div>
    <ul v-if="todos && todos?.items"> TODOS:
      <li v-for="todo in todos.items" :key="todo.id">#{{ todo.id }}: {{ todo.txt }} </li>
    </ul>

  </main>
</template>
