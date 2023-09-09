<template>
<TransitionRoot :show="isOpen" enter='transform transition ease-in-out duration-1000' enterFrom='translate-x-full' enterTo='translate-x-0' leave="transition ease-in-out duration-1000 transform" leave-from="translate-x-0" leave-to="translate-x-50" class="flex absolute justify-center items-center w-80 p-1.5 right-8 -mr-2 top-5 mb-4 font-base bg-[#1ED760]  border  rounded-md shadow" role="alert">
    <div class="inline-flex items-center justify-center flex-shrink-0 text-white">
        <svg aria-hidden="true" class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
        </svg>
        <span class="sr-only">Check icon</span>
    </div>
    <div v-if="action === 'delete'" class="ml-3 text-xs text-white font-base">{{ item }} removed from the system</div>
    <div v-if="action === 'add'" class="ml-3 text-xs text-white font-base">{{ item }} added to the system</div>
    <div v-if="action === 'edit'" class="ml-3 text-xs text-white font-base">{{ item }} successfully updated</div>
    <div v-if="action === 'copy'" class="ml-3 text-xs text-white font-base">{{ item }} successfully copied</div>
</TransitionRoot>
</template>
<script>
import {
    TransitionRoot,
    TransitionChild,
} from '@headlessui/vue'
export default {
    components: {
        TransitionRoot,
        TransitionChild,
    },
    data() {
        return {
            isOpen: false,
            item: "",
            action: ""
        }
    },
    methods: {
        toggleModal() {
            this.isOpen = !this.isOpen
        }
    },
    mounted() {
        this.emitter.on("showNotification", data => {
            this.item = data.item
            this.action = data.action
            this.toggleModal()
            setTimeout(() => this.isOpen = false, 2000)
        })
    }
}
</script>
