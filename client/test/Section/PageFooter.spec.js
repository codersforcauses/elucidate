import { mount } from '@vue/test-utils';
import PageFooter from '@/components/Section/PageFooter.vue';
describe('PageFooter', () => {
  test('is a Vue instance', () => {
    const wrapper = mount(PageFooter);
    expect(wrapper.vm).toBeTruthy();
  });

  test('renders correctly', () => {
    const wrapper = mount(PageFooter);
    expect(wrapper.element).toMatchSnapshot();
  });
});
