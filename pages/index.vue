<template>
  <div>
    <Header />
    <Homepage/>
    <Footer/>

  </div>

</template>

<script>
export default {
  mounted() {
    this.$router.push({path: '/login'})
  },
};
</script>