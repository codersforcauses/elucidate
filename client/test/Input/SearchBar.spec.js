import SearchBar from '@/components/Input/SearchBar.vue';
import { mount } from '@vue/test-utils';

describe('SearchBar', () => {
  it('is a Vue instance', () => {
    const wrapper = mount(SearchBar);
    expect(wrapper.vm).toBeTruthy();
  });

  it('renders correctly', () => {
    const wrapper = mount(SearchBar);
    expect(wrapper.element).toMatchSnapshot();
  });

  it('accepts text', () => {
    const wrapper = mount(SearchBar);
    wrapper.find('input').setValue('Test');
    expect(wrapper.find('input').element.value).toBe('Test');
  });
});
