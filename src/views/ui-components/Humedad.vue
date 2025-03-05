<script setup lang="ts">
import { ref } from 'vue';
/*import tabler icons*/
import { TrashIcon, SendIcon, BellIcon } from 'vue-tabler-icons';
// icons
import { AccessPointIcon } from 'vue-tabler-icons';
import OutlinedButtons from '@/components/ui-components/button/OutlinedButtons.vue';
import Humedad1 from '@/components/ui-components/button/Humedad1.vue';
import Humedad2 from '@/components/ui-components/button/Humedad2.vue';
import TablaHum from '@/components/dashboards/TablaHum.vue';
// buttons color data
const btnsColor = ref(['primary', 'secondary', 'success', 'error', 'warning']);

</script>

<template>
    <v-row>
        <v-col cols="12">

                <v-row>
                    <!-- Base Buttons -->
                    <v-col cols="12" sm="12">
                        <UiChildCard title="Default">
                            <Humedad1 />
                        </UiChildCard>
                    </v-col>
                    <!-- Color Buttons -->
                    <v-col cols="12" lg="6">
                        <UiChildCard title="Colors">
                            <Humedad2 />
                        </UiChildCard>
                    </v-col>
                    <!-- tiempos de actulizacion -->
                    <v-col cols="12" sm="12" lg="12">
                        <TablaHum/>
                    </v-col>
                </v-row>
        </v-col>
    </v-row>
</template>
