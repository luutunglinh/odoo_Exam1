<template>
  <div class="toast">
    <div class="toast_message">
      <span>{{ content }}</span>
    </div>
  </div>
</template>
<script>
export default {
  name: 'MToast',
  created () {},
  props: {
    content: String,
    title: String
  },
  methods: {
  }
}
</script>
<style lang="css" scoped>
.toast {
  position: absolute;
  display: inline-flex;
  padding: 6px 12px;
  justify-content: center;
  align-items: center;
  border: 1px solid #EB1F1F;
  background: #F4E3E3;
  right: 32%;
  transform: translate(10px, 13px);
}

.toast_message {
  color: #EB1F1F;
  font-family: Inter;
  font-size: 14px;
  font-style: normal;
  font-weight: 500;
  line-height: 20px; /* 200% */
}

</style>
