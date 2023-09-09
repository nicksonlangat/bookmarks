<template>
<div v-if="verified && !passwordReset" class="flex mx-4 lg:mx-0 flex-col items-center text-stone-300 font-base justify-center">
    <div class="mt-32 lg:w-1/3 w-full">
        <h3 class="text-3xl">Reset your password</h3>
        <h3 class="mt-5 text-lg text-stone-400">Please set a new password</h3>
    </div>
    <form class="w-full lg:w-1/3 mt-10 flex flex-col gap-8">
        <div class="flex flex-col gap-2 text-stone-300">
            <label for="">New Password</label>
            <input v-model="user.password" type="password" class="bg-[#111111] px-6 py-2 rounded-md focus:outline-none focus:right-0">

        </div>
        <div class="flex flex-col gap-2 text-stone-300">
            <label for="">Confirm Password</label>
            <input v-model="user.confirm_password" type="password" class="bg-[#111111] px-6 py-2 rounded-md focus:outline-none focus:right-0">

        </div>
        <button @click.prevent="submitRequest" class="bg-[#6c53cd] rounded-md text-stone-100 py-2">Reset password</button>

    </form>
</div>
<div v-if="passwordReset" class="flex mx-4 lg:mx-0 flex-col items-center text-stone-300 font-base justify-center">
    <div class="mt-32 lg:w-1/3 w-full">
        <h3 class="mt-32 text-3xl">Password reset!</h3>
        <h3 class="mt-5 text-lg text-start text-stone-400">Your password has been reset. Please login to your account.</h3>
    </div>
    <a href="/login" class="bg-[#6c53cd] text-center mt-10 w-full lg:w-1/3 rounded-md text-stone-100 py-2">Go to login</a>
</div>
<div v-if="!verified" class="flex mx-4 lg:mx-0 flex-col items-center text-stone-300 font-base justify-center">
    <div class="mt-32 lg:w-1/3 w-full">
        <h3 class="mt-32 text-3xl">Invalid token</h3>
        <h3 class="mt-5 text-lg text-start text-stone-400">The token is invalid or has expired. Please request a new one.</h3>
    </div>
    <a href="/reset" class="bg-[#6c53cd] text-center mt-10 w-full lg:w-1/3 rounded-md text-stone-100 py-2">Request new token</a>
</div>
</template>

<script>
import {
    mapActions
} from 'vuex'
export default {
    name: 'Reset-Password',
    data() {
        return {
            user: {
                password: "",
                confirm_password: ""
            },
            verified: false,
            uidb64: "",
            token: "",
            passwordReset: false,
        }
    },
    methods: {
        ...mapActions({
            verifyResetToken: 'verifyResetToken',
            resetPassword: 'resetPassword'
        }),
        submitRequest() {
            this.resetPassword({
                payload: {
                    "password": this.user.password,
                    "uidb64": this.uidb64
                },
                cb: (() => {
                    this.passwordReset = true
                })
            })

        },
        async verifyToken(uidb4, token) {
            await this.verifyResetToken({
                uidb4: uidb4,
                token: token,
                cb: ((res) => {
                    if (res.success) {
                        this.verified = true
                    } else {

                    }
                })
            })

        }
    },
    mounted() {
        this.uidb64 = this.$route.query['uidb64']
        this.token = this.$route.query['token']

        this.verifyToken(this.uidb64, this.token)

    }
}
</script>

<style>
html {
    background-color: #040405;
}
</style>
