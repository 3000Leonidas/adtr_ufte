<script setup lang="ts">
import { ref } from 'vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

import Closable from '@/components/ui-components/alert/Closable.vue';
import TablaTemp from '@/components/dashboards/TablaTemp.vue';

</script>

<template>
    <v-row>
        <v-col cols="12">
            <v-row>
             
                <!-- Filled -->
                <v-col cols="12">
                    
                </v-col>
                <!-- Closable -->
                <v-col cols="12">
                    <UiChildCard title="Alert Closable">
                        <Closable />
                    </UiChildCard>
                </v-col>
                <!-- Basic -->      
                <v-col cols="12" sm="12" lg="12">
                <TablaTemp/>
                </v-col>
            </v-row>
        </v-col>
    </v-row>
</template>
