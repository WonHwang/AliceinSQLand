<template>
    <div>
      <unity
      src = "./unity/Build/webGL.json"
      unityLoader = "./unity/Build/UnityLoader.js"
      ref = "hookInstance"
      :height = height
      :width = width
      >
      </unity>
    </div>
</template>
<script>
import Unity from 'vue-unity-webgl';
export default {
    name : "Unity",
    data() {
        return {
            height : '700',
            width : '950',
        }
    },
    components : {Unity},
}
</script>
<style scoped>
</style>