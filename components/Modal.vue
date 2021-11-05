<template>
    <b-modal id="bv-modal-example" hide-footer> 
      <template #modal-title> <img src="../assets/img/LMS.png" class="rounded me-2" alt="" width="10%"/>AIO Alerts </template>
      <div class="d-block text-center">
        <h3>{{message}}</h3>
      </div>
    </b-modal>
</template>

<script>
export default {
    props: ['message']
}
</script>

