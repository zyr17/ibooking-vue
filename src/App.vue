<template>
  <div id="app">
    <p class="tab">
      <span v-if="$store.state.role != 'none'">你好，{{ $store.state.role == 'admin' ? '管理员' : '用户' }} {{ $store.state.name ? $store.state.name : '' }}</span>
      <router-link v-if="$store.state.role == 'none'" to="/register" class="btn btn-primary">注册</router-link>
      <router-link v-if="$store.state.role == 'none'" to="/login" class="btn btn-primary">登录</router-link>
      <router-link v-if="$store.state.role == 'user'" to="/personal_info" class="btn btn-primary">个人信息</router-link>
      <router-link v-if="$store.state.role == 'user'" to="/checkin" class="btn btn-success">签到</router-link>
      <router-link v-if="$store.state.role == 'user'" to="/book" class="btn btn-primary">预约</router-link>
      <router-link v-if="$store.state.role == 'user'" to="/history" class="btn btn-primary">历史</router-link>
      <router-link v-if="$store.state.role == 'admin'" to="/all_students" class="btn btn-primary">用户管理</router-link>
      <router-link v-if="$store.state.role == 'admin'" to="/all_studyrooms" class="btn btn-primary">自习室管理</router-link>
      <router-link v-if="$store.state.role == 'admin'" to="/card_checkin" class="btn btn-success">刷卡签到</router-link>
      <button v-if="$store.state.role != 'none'" @click="logout" class="btn btn-primary">登出</button>
    </p>
    <p class="tab" v-if="false">
      <router-link to="/register" class="btn btn-primary">注册</router-link>
      <router-link to="/login" class="btn btn-primary">登录</router-link>
      <router-link to="/personal_info" class="btn btn-primary">个人信息</router-link>
      <router-link to="/checkin" class="btn btn-success">签到</router-link>
      <router-link to="/book" class="btn btn-primary">预约</router-link>
      <router-link to="/history" class="btn btn-primary">历史</router-link>
      <router-link to="/all_students" class="btn btn-primary">用户管理</router-link>
      <router-link to="/all_studyrooms" class="btn btn-primary">自习室管理</router-link>
      <router-link to="/card_checkin" class="btn btn-success">刷卡签到</router-link>
    </p>
    <router-view></router-view>
    <div id="notification-div">
      <notification></notification>
    </div>
  </div>
</template>

<style>
    .fade-enter-active, .fade-leave-active {
      transition: opacity .5s
    }
    .fade-enter, .fade-leave-active {
      opacity: 0
    }

    #notification-div {
        position: fixed;
        width: 20%;
        margin: 1%;
        left: 78%;
        top: 0%;
    }
</style>

<script>
import store from './store'
import Notifications from './components/notifications.vue';

console.log(store)

export default {
    data() {
        return {};
    },
    store,
    methods: {
        logout() {
            this.$store.commit("clearAuth");
            localStorage.clear();
            store.commit('setNotification', {
              type: "success",
              message: "登出成功",
            })
            this.$router.push("/login");
        }
    },
    created: () => {
    },
    name: "app",
    components: { notification: Notifications }
};
</script>
