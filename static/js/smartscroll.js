import {default as debounce} from './debounce';
export default function(fn, threshold){
  return fn ? 
    this.bind('scroll', this.sras_scroll = debounce(fn, threshold)) : 
    this.trigger('smartscroll'); 
}