<script setup>
import { ref, onMounted } from 'vue';
import UiChildCard from '@/components/shared/UiChildCard.vue';

const users = ref([]);
const errorMessage = ref('');

onMounted(async () => {
    try {
        const response = await fetch('/api/users'); // Elimina el encabezado Authorization

        if (response.ok) {
            users.value = await response.json();
            errorMessage.value = '';
        } else {
            const errorData = await response.json();
            errorMessage.value = errorData.message || 'Error al obtener usuarios.';
            console.error('Error:', response.status, response.statusText);
        }
    } catch (error) {
        errorMessage.value = error.message;
        console.error('Error:', error);
    }
});
</script>

<template>
    <div>
        <div v-if="errorMessage">{{ errorMessage }}</div>
    </div>

    <v-row class="month-table">
        <v-col cols="12" sm="12">
            <UiChildCard title="Tabla de usuario">
                <v-table fixed-header height="300px">
                    <thead>
                        <tr>
                            <th class="text-left">Name</th>
                            <th class="text-left">Acceso</th>
                            <th class="text-left">Correo</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="user in users" :key="user.username">
                            <td>{{ user.username }}</td>
                            <td>{{ user.role }}</td>
                            <td>{{ user.email }}</td>
                        </tr>
                    </tbody>
                </v-table>
                <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
            </UiChildCard>
        </v-col>
    </v-row>
</template>