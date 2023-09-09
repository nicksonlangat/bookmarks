<template>
<div class="flex mx-4 lg:mx-0 flex-col items-center text-stone-300 font-base justify-center">
    <div v-if="!emailSent" class="mt-32 w-full lg:w-1/3">
        <h3 class="text-3xl text-center">Forgot password?</h3>
        <h3 class="text-lg mt-5 text-center text-stone-400">Enter your email address and we will send instructions to reset it.</h3>

    </div>
    <form v-if="!emailSent" class="w-full lg:w-1/3 mt-10 flex flex-col gap-8">
        <div class="flex flex-col gap-2 text-stone-300">
            <label for="">Email</label>
            <input v-model="user.email" type="email" class="bg-[#111111] focus:bg-[#111111] border border-stone-900 px-6 py-2 rounded-md focus:outline-none focus:right-0">
        </div>
        
        <button @click.prevent="submitPasswordResetRequest" class="bg-[#6c53cd] rounded-md text-stone-100 py-2">Proceed</button>
        <div class="flex justify-center text-stone-500 underline"><a href="/login">Go back to log in</a></div>
    </form>
    <div v-if="emailSent" class="mt-32 w-full lg:w-1/3">
        <h3 class="text-3xl text-center">Email sent!</h3>
        <h3 class="text-lg mt-5 text-center text-stone-400">We have sent reset instructions to {{ user.email }}. Please check your inbox now.</h3>
    </div>
    
</div>
</template>
<script>
import {
    mapActions
} from 'vuex'
export default {
    name: 'Reset',
    data() {
        return {
            user: {
                email: "nicksonlangat95@gmail.com"
            },
            emailSent: false
        }
    },
    methods: {
        ...mapActions({
            resetPasswordRequest: 'resetPasswordRequest'
        }),
        submitPasswordResetRequest() {
            this.resetPasswordRequest({
                payload: this.user,
                cb: (() => {
                    this.emailSent = true
                })
            })

        }
    }
}
</script>
<style>
html {
    background-color: #040405;
}
</style>
