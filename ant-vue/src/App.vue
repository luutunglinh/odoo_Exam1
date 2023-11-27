<template>
  <div class="content">
    <TheSidebar></TheSidebar>
    <div class="content__right">
      <TheHeader></TheHeader>
      <TheMain></TheMain>
    </div>
  </div>
</template>
<script>
import TheHeader from './components/layout/TheHeader.vue'
import TheMain from './components/layout/TheMain.vue'
import TheSidebar from './components/layout/TheSidebar.vue'
export default {
  name: 'App',
  components: {
    TheSidebar,
    TheHeader,
    TheMain
  }
}
</script>

<style lang="css">
@import url(components/css/main.css);
@import url(components/base/btn.css);
</style>
