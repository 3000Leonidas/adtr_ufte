<script setup lang="ts">
import { UserIcon, MailIcon, ListCheckIcon, LogoutIcon } from 'vue-tabler-icons';
import { useRouter } from 'vue-router';
const router = useRouter();

const logout = async () =>  {
    try {
    const response = await fetch('/api/logout', {
      method: 'POST',
    });
    if (response.ok) {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      localStorage.removeItem('userRole'); // Limpia el rol
      router.push('/auth/login'); // Redirige a la página de inicio de sesión
    } else {
      console.error('Logout failed:', response.status, response.statusText);
    }
  } catch (error) {
    console.error('Logout error:', error);
  }
};
</script>


<template>
    <!-- ---------------------------------------------- -->
    <!-- notifications DD  -->
    <!-- ------------------Barra de notificacion e icono del usaurio---------------------------- -->
    <v-menu :close-on-content-click="false">
        <template v-slot:activator="{ props }">
            <v-btn class="" variant="text" v-bind="props" icon>
                <v-avatar size="35">
                    <img src="@/assets/images/profile/user-1.jpg" height="35" alt="user" />
                </v-avatar>
            </v-btn>
        </template>
        <v-sheet rounded="xl" width="200" elevation="10" class="mt-2">
            <v-list class="py-0" lines="one" density="compact">
                <!--<v-list-item value="item1" color="primary" >
                    <template v-slot:prepend>
                        <UserIcon stroke-width="1.5" size="20"/>
                    </template>
                    <v-list-item-title class="pl-4 text-body-1">Mi perfil</v-list-item-title>
                </v-list-item>-->
            </v-list>
            <div class="pt-4 pb-4 px-5 text-center">
                <v-btn @click="logout" color="primary" variant="outlined" class="rounded-pill" block>Cerrar Sesión</v-btn>
            </div>
        </v-sheet>
    </v-menu>
</template>
