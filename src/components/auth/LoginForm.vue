<script setup lang="ts">
import { ref } from 'vue';
const checkbox = ref(false);

const username=ref('');
const password=ref('');
const errorMensaje=ref('');

const login = async () => {
  errorMensaje.value = '';
  if (!username.value || !password.value) {
    errorMensaje.value = 'Usuario y contraseña son requeridos';
    return;
  }
  try {
    const response = await fetch('/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: username.value,
        password: password.value,
      }),
    });
    if (response.ok) {
      const data = await response.json();
      localStorage.setItem('token', data.token);
      localStorage.setItem('user', JSON.stringify(data.user));
      if (data.role) {
        localStorage.setItem('userRole', data.role); // Almacena el rol
      } else {
        console.error('Role not found in response from backend.');
      }
      window.location.href = 'http://localhost:5173/';
    } else if (response.status === 401) {
      const errorData = await response.json();
      errorMensaje.value = errorData.message || 'Credenciales Invalidas';
    } else {
      errorMensaje.value = 'Error al iniciar sesión. Inténtalo de nuevo más tarde.';
      console.error('Error en la solicitud', response.status, response.statusText);
    }
  } catch (error) {
    errorMensaje.value = 'Error al iniciar sesión. Inténtalo de nuevo más tarde.';
    console.error('Error en la solicitud', error);
  }
};
</script>



<template>
    <div class="d-flex align-center text-center mb-6">
        <div class="text-h6 w-100 px-5 font-weight-regular auth-divider position-relative">
            <span class="bg-surface px-5 py-3 position-relative text-subtitle-1 text-grey100">Resgistro DMIC 1.0</span>
        </div>
    </div>
    <div>
        <v-row class="mb-3">
            <v-col cols="12">
                <v-label class="font-weight-medium mb-1">Usuario</v-label>
                <v-text-field v-model="username" variant="outlined" class="pwdInput" hide-details color="primary"></v-text-field>
            </v-col>
            <v-col cols="12">
                <v-label class="font-weight-medium mb-1">Constraseña</v-label>
                <v-text-field v-model="password" variant="outlined" class="border-borderColor" type="password" hide-details color="primary"></v-text-field>
            </v-col>
            <v-col cols="12 " class="py-0">
                <div class="d-flex flex-wrap align-center w-100 ">
                    <v-checkbox hide-details color="primary">
                        <template v-slot:label class="">Recuerde este dispositivo</template>
                    </v-checkbox>
                    <div class="ml-sm-auto">
                        <RouterLink to=""
                            class="text-primary text-decoration-none text-body-1 opacity-1 font-weight-medium">
                            ¿Has olvidado tu contraseña?</RouterLink>
                    </div>
                </div>
            </v-col>
        <v-col cols="12">
            <v-btn size="large" rounded="pill" color="primary" class="rounded-pill" block @click="login" flat>Iniciar Sesión</v-btn>
            <div v-if="errorMensaje" class="error-menssage">{{ errorMensaje }}</div>
        </v-col>
        </v-row>
    </div>
</template>
