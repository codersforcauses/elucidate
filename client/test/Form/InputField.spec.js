import { mount } from '@vue/test-utils';
import InputField from '@/components/Form/InputField.vue';

describe('InputField', () => {
  it('is a Vue instance', () => {
    const wrapper = mount(InputField);

    expect(wrapper.vm).toBeTruthy();
  });

  it('has a label', () => {
    const wrapper = mount(InputField, {
      props: { fieldName: 'Test InputField' },
    });
    const label = wrapper.find('[data-test="formTextBoxLabel"]');

    expect(label.text()).toBe('Test InputField');
  });

  it('has a password variant with show button', () => {
    const wrapper = mount(InputField, {
      fieldName: 'Test InputField',
      fieldType: 'password',
    });
    const subtext = wrapper.find('[data-test="formTextBoxLabel"]');

    expect(subtext.text()).toBe('Test Subtext');
  });

  it('can validate passwords', () => {
    const wrapper = mount(InputField, {
      fieldName: 'Test InputField',
      fieldType: 'password',
      rules: 'password:T3stP@ssword',
    });
    const subtext = wrapper.find('[data-test="formTextBoxLabel"]');

    expect(subtext.text()).toBe('Test Subtext');
  });
});
