import ButtonElement from '@/components/Input/ButtonElement.vue';
import { mount } from '@vue/test-utils';

describe('ButtonElement', () => {
  it('is a Vue instance', () => {
    const wrapper = mount(ButtonElement);
    expect(wrapper.vm).toBeTruthy();
  });

  it('renders correctly', () => {
    const wrapper = mount(ButtonElement);
    expect(wrapper.element).toMatchSnapshot();
  });

  it('displays text', () => {
    const wrapper = mount(ButtonElement, {
      slots: {
        default: 'Test',
      },
    });
    expect(wrapper.find('button').text()).toBe('Test');
  });
});
