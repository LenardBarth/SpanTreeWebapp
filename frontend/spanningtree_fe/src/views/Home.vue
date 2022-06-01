<template>
    <div>
        <h1>VUE Hompeage</h1>
    </div>
    <button class="btn btn-primary" @click="$emit('infoPopup', {status: 'primary', msg: 'This is a test PRIMARY message'})">Test Alert Primary</button>
    <button class="btn btn-success" @click="$emit('infoPopup', {status: 'success', msg: 'This is a test SUCCESS message'})">Test Alert Success</button>
    <button class="btn btn-warning" @click="$emit('infoPopup', {status: 'warning', msg: 'This is a test WARNIING message'})">Test Alert Warning</button>
    <button class="btn btn-danger" @click="$emit('infoPopup', {status: 'danger', msg: 'This is a test DANGER message'})">Test Alert Danger</button>
</template>

<script>
export default {
    name: "HomePage",
    emits: ['infoPopup']
}
</script>

<style>
button {
    margin: 5px;
}
</style>