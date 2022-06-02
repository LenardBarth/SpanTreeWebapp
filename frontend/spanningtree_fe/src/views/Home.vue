<template>
<div class="content-wrapper">
    <!-- List Layout and Funcionalty from https://codepen.io/SimoTuognia/pen/ZjYJQo -->
    <div class="component-wrapper">
        <addVrtxListVue />
    </div>
    <div class="component-wrapper">
        <addEdgeListVue />
    </div>
</div>
</template>

<script>
import addVrtxListVue from '@/components/addVrtxList.vue'
import addEdgeListVue from '@/components/addEdgeList.vue'

export default {
    name: "HomePage",
    components: {
        addVrtxListVue,
        addEdgeListVue
    },
    emits: ['infoPopup']
}
</script>

<style scoped>
.content-wrapper {
    width: 100vw;
    display: flex;
    justify-content: space-between;
}
.component-wrapper {
    width: 49%;
    margin: 5px;
}
</style>